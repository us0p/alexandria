# Context package
Defines the Context type, which carries deadlines, cancellation signals, 
and other request-scoped values across API boundaries and between 
processes.  

Incoming requests to a server should create a `Context`, and outgoing calls 
to servers should accept a Context. The chain of function calls between 
them must propagate the `Context`, optionally replacing it with a derived 
Context created using `WithCancel`, `WithDeadline`, `WithTimeout`, or 
`WithValue`. 
When a `Context` is canceled, all Contexts derived from it are also 
canceled.  

The `WithCancel`, `WithDeadline`, and `WithTimeout` functions take a 
`Context` (the parent) and return a derived `Context` (the child) and a 
`CancelFunc`.  
Failing to call the `CancelFunc` leaks the child and its children until the
parent is canceled or the timer fires. The go vet tool checks that 
`CancelFuncs` are used on all control-flow paths.  

The `WithCancelCause` function returns a `CancelCauseFunc`, which takes an
error and records it as the cancellation cause. Calling Cause on the 
canceled context or any of its children retrieves the cause. If no cause is
specified, `Cause(ctx)` returns the same value as `ctx.Err()`.

Programs that use `Contexts` should follow these rules to keep interfaces 
consistent across packages and enable static analysis tools to check 
context propagation:  
- Do not store `Contexts` inside a struct type; instead, pass a `Context` 
explicitly to each function that needs it.
- The `Context` should be the first parameter, typically named `ctx`.

```go
func DoSomething(ctx context.Context, arg Arg) error {
	// ... use ctx ...
}
```

- Do not pass a nil Context, even if a function permits it. Pass 
`context.TODO` if you are unsure about which `Context` to use.  
- The same `Context` may be passed to functions running in different 
goroutines;
- `Contexts` are safe for simultaneous use by multiple goroutines.  
- Propagated `Context` must be checked upon `ctx.Done()` to validade 
context cancelation throughout the routines.  
## Context Factories
**Background**  
Returns a non-nil, empty `Context`, It's never canceled, has no values, and
has no deadline.  
It's typically used by the main function, initialization, tests, and as the
top-level Context for incoming requests.  
  
**TODO**  
Returns a non-nil, empty `Context`. Code should use `context.TODO` when 
it's unclear which context to use or it's not yet available (because the 
surrounding function has not yet been extended to accept a Context 
parameter).  
  
## Derived Factories
**WithValue**  
Retutns a copy of the parent associating key with value.  
The provided key must be comparable and should not be of type string or any
other built-in type to avoid collisions between packages using context.  
Users of `WithValue` shoudl define their own types for keys.  
To avoid allocating when assigning to an `interface{}`, context keys often
have concrete type `struct{}`.  
  
**WithCancel**  
Returns a copy of parent with a new `Done channel`. The returned context's
`Done channel` is closed when the returned cancel function is called or 
when the parent context's `Done channel` is closed, whichever happens 
first.  
  
**WithDeadline**  
Returns a copy of the parent context with the deadline adjusted to be no 
later than the provided `time.Time` d.  
The returned `Context.Done` channel is closed when the deadline expires, 
when the returned cancel function is called, or when the parent context's 
`Done channel` is closed, whichever happens first.  
Even though ctx will be expired, it is good practice to call its 
cancellation function in any case. Failure to do so may keep the context 
and its parent alive longer than necessary, like when the routine is 
completed before the deadline.  
  
**WithTimeout**  
WithTimeout returns `WithDeadline(parent, time.Now().Add(timeout))`.  
  
## Cleanup
**AlterFunc**  
Arranges to call the provided `callback` in its own goroutine after `ctx` 
is done (canceled or timed out). If `ctx` is already done, `AfterFunc` 
calls callback immediately in its own goroutine.  
Multiple calls to `AlterFunc` on a context operate independently; one does 
not replace another.  
Calling the returned stop function stops the association of `ctx` with 
callback. It returns true if the call stopped callback from being run. If 
stop returns false, either the context is done and callback has been 
started in its own goroutine; or callback was already stopped. The stop 
function does not wait for callback to complete before returning. If the 
caller needs to know whether callback is completed, it must coordinate with
callback explicitly. If `ctx` has a `"AfterFunc(func()) func() bool"` 
method, `AfterFunc` will use it to schedule the call.  
  
## Best Practices
1. **Pass Context Explicity**: Always pass the context as an explicit 
   argument to functions or goroutines instead of using global variables.
2. **Avoid Using context.Background()**: Instead of using 
   `context.Background()` directly, create a specific context using 
   `context.WithCancel()` or `context.WithTimeout()` to manage its 
   lifecycle and avoid resource leaks.
3. **Keep Context Size Small**: Avoid storing large or unnecessary data in
   the context. Only include the data required for the specific operation.
4. **Avoid Chaining Contexts**: Chaining contexts can lead to confusion and 
   make it challenging to manage the context hierarchy. Instead, propagate
   a single context throughout the application.
5. **Be Mindful of Goroutine Leaks**: Always ensure that goroutines 
   associated with a context are properly closed or terminated to avoid 
   goroutine leaks.
