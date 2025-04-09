## Edge locations
Is a site that Amazon `CloudFront` uses to store cached copies of your content closer to your customers for faster delivery.
- **Origin:** Is where your content is generated.
- **Edge location:** Instead of requiring your customers to get their data from the `origin`, you can cache copy locally at an edge location that is close to your customers.
- **Customer:** When a customer in another Region requests one of your files, Amazon `CloudFront` retrieves the file from the cache in the edge location and delivers the file to the customer. The file is delivered to the customer faster because it came from the edge location near the customer [Regions](aws_region.md) instead of the original source in origin.
 
Caching copies of data closer to the customers all around the world uses the concept of `content delivery networks`, or CDN.

An CDN is a network that delivers edge content to users based on their geographic location. Amazon `CloudFront` is a service that helps deliver data, video, applications, and APIs to customers around the world with low latency and high transfer speeds.

Edge locations, also run more than just `CloudFront`. They run a domain name service, or [DNS](aws_networking.md#Domain%20Name%20System%20-%20DNS), known as `Amazon Route 53`, helping direct customers to the correct web locations with reliably low latency.

AWS Outposts, is a service where AWS basically install a fully operational mini Region, right inside your own data center. That's owned and operated by AWS, using 100% of AWS functionality, but isolated within your own building.
