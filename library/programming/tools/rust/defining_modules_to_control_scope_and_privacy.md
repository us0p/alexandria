- **Start from the crate root**: When compiling a crate, the compiler first looks in the crate root file for code to compile
- **Declaring modules**: In the crate root file, you can declare new modules. The compiler will look for the module's code in these places:
	- Inline, within curly brackets that replace the semicolon following `mod <module_name>`
	- In the `src/<module_name>.rs`
	- In the file `src/<module_name>/mod.rs` -> old style
- **Declaring sub-modules**: In any file other than the crate root, you can declare sub-modules. The compiler will look for the sub-module's code within the directory named for the parent module in these places:
	- Inline, directly following `mod <module_name>`, within curly brackets instead of the semicolon
	- In the file `src/<parent_module>/<module_name>.rs`
	- In the file `src/<parent_module>/<module_name>/mod.rs` -> old style
- **Paths to code in modules**: Once a module is part of your crate, you can refer to code in that module from anywhere else in that same crate, as long as the privacy rules allow, using the path to code.
- **Private vs. Public**: Code within a module is private from its parent modules by default. To make a module public, declare it with `pub mod` instead of `mod`. To make items within a public module public as well, use `pub` before their declarations.
- **The `use` keyword**: Within a scope, the `use` keyword creates shortcuts to items to reduce repetition of long paths.

Note that you only need to load a file using `mod` declaration once in your module tree. Once the compiler knows the file is part of the project and knows where in the module tree the code resides (because of where you've put the `mod` statement), other files in your project should refer to the loaded file's code using a path to where it was declared. In other words, `mod` is not an "include" operation that you may have seen in other programming languages.

If you use both styles (old and new) for the same module, you'll get a compile error. Using a mix of both styles for different modules in the same project is allowed, but might be confusing for people navigating your project.