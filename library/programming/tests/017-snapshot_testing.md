# Snapshot testing
software technique where you capture a snapshot (a serialized representation) of a component output and compare it against a previously saved version, ensuring that changes don't introduce unexpected UI or data issues.
It acts as a form of regression testing.
It's type of "output comparison" testing. It prevent regressions by comparing the current characteristics of an application or component with stored "good" values for those characteristics.
Snapshot tests are sometimes mistaken for UI testing, they serve different purposes. Snapshot tests are designed to assess how content is displayed across various setups and screen sizes. On the other hand, UI tests focus on what is displayed on the screen.
should be used if you have static views that don't change visually.
## How it works
- A component or function is rendered, and its output is captured
- This captured output is saved as a "snapshot" file, which is stored alongside the test.
- During subsequent test runs, the current output is compared to the saved snapshot. This comparison is done pixel by pixel.
- If the outputs match, the test passes; if they differ, the test fails, indicating a potential issue.
Note that snapshot tests can pass even when they new capture isn't pixel-perfect to the reference. This happens because precision and perceptual precision.
By default, precision is set to 100%, meaning each pixel of the capture should match each pixel of the reference. However, in some cases, we may not want to go for 100% precision because it might be cause our tests to fail.
For example, a common reason for failing tests are minor differences in interfaces arising from different architectures or due to anti-aliasing. To avoid this, we can decrease the precision by 0.01 to 0.04, depending on how much we need these failing tests (that are fundamentally matching) to pass.
Perceptual precision is "the percentage a pixel must match the source pixel to be considered a match". This means that pixels get compared on the basis of how similar they are according to the human eye.
Pay attention to your failing tests and make sure the reason they are failing is really some factor like those mentioned above and not a human error.
## Benefits
- provides a straightforward way to ensure that the output of a component or function remains consistent.
- helps catch unintended changes in the output that might be missed by traditional unit or functional tests.
- focus on the output of a component, rather than the internal implementation details.
- Effective tool for preventing regressions in an application.
## Drawbacks
- must store external resources like images and more in the project to avoid clumsy tests.
- create extra work if your views change often as the snapshots will fail often.
- tightly coupled to an application output, which makes them very fragile. developers then must manually verify that everything is still working properly and update the snapshots.
- Snapshot tests aren't well suited to dynamic content. A "random quote of the day" component will frequently fail snapshot tests. Certain types of dynamic content can be even more problematic for example JavaScript and CSS animations. Tools can deal with this problem by letting users mark areas with dynamic content.
- Storage requirements. Snapshots must be store somewhere; typically they're checked into the project repository. Cloud-based services can provide some assistance by storing snapshots for visual tests.