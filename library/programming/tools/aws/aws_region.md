# AWS Regions
Throughout the globe, AWS builds Regions to be closest to where the business traffic demands. Locations like Paris, Tokyo, Sao Paulo, Dublin, Ohio.

Inside each Region, we have multiple data centers that have all the compute, storage, and other services you need to run your applications. 

Each Region can be connected to each other Region through a high speed fiber network, controlled by AWS. it's important to know that you, the business decision maker, gets to choose which Region you want to run out of. And each Region is isolated from every other Region in the sense that absolutely no data goes in or out of your environment in that Region without you explicitly granting permission for that data to be moved.
  
When determining the right Region for your services, data, and applications, consider the following four business factors:
- **Compliance with data governance and legal requirements:** Depending on your company and location, you might need to run your data out of specific areas. For example, if your company requires all of its data to reside within the boundaries of the UK, you would choose the London  Region.
- **Proximity to your customers:** Selecting a Region that is close to your customers will help you to get content to them faster. 
- **Available services within a Region:** Sometimes, the closest Region might not have all the features that you want to offer to customers. AWS is frequently innovating by creating new services and expanding on features within existing services. However, making new services available around the world sometimes requires AWS to build out physical hardware one Region at a time.
- **Pricing:** Pricing can vary from Region to Region.