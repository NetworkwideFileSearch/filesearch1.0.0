
When to Use SQL vs. NoSQL
Are you thinking of making the leap from SQL to NoSQL and wondering whether it’s the right move?



The difference between SQL and NoSQL databases is really just a comparison of relational vs. non-relational databases. Deciding when to use SQL vs. NoSQL depends on the kind of information you’re storing and the best way to store it. Both types store data, they just store data differently.


Asking NoSQL or SQL is akin to asking the hotly debated internet discussion, “Is it Yanny or Laurel?” People want to give definitive answers, but the real answer is it depends on what you’re building, constraints dictated by who you’re building for, and the end state you are trying to achieve.



While NoSQL is trending and the adoption rate is rising, it’s not a replacement for SQL. It’s just another option. Sometimes it’s about choosing one over the other, but many development teams opt to use both.



In this article we will:

Review the main differences between SQL vs. NoSQL databases
Share examples of when to use SQL vs. NoSQL and factors to consider in your decision Let’s start with a quick explanation of SQL and NoSQL.



What is NoSQL and Why Does it Exist?

Kim Kardashian infamously tried to break the internet, but NoSQL saved us. With the rise of social media, Ecommerce, search, and the explosion of data, SQL was struggling to manage all the requests, transactions, and activity occurring online. NoSQL is designed to manage lots of traffic and data.




Yes, SQL came first. It’s used to communicate with relational databases. Relational databases store data in a very organized, but also rigid way. NoSQL, earning it’s name by being “not only SQL” makes it easier to store all different types of data together. It’s used for its flexibility and therefore speed and scalability in managing large volumes of data.



Today we have many options like MongoDB, Cassandra, Redis, Couchbase, DynamoDB, and Cosmos DB gaining in popularity, growing user communities, and quickly adding more and more features. There are also four types of NoSQL databases.


Key Value:

Data is stored as attribute names or keys with values 

Document: contains many different key value pairs 
Graph: used to store data related to connections or networks 
Column: data is stored as columns instead of rows 
Each type of NoSQL database stores data differently and is selected and used in different contexts. For example, graph databases are commonly used in social media.


SQL vs. NoSQL Scalability

One of the main issues with SQL is ease of scalability. SQL is designed to scale up. What we mean by “scaling up” or scaling vertically is adding extra hardware, RAM, processing power, etc. in order to increase capacity. With SQL we’re limited because we will inevitably max out on capacity and scaling up is expensive. Scaling out with SQL is possible, but requires extensive effort (partitioning, sharding, clustering, etc.) and cost.



Here’s the key difference when comparing SQL vs. NoSQL scalability: NoSQL engines are designed to scale out and leverage cloud computing. When scaling out or horizontally we are adding resources to a single node (a computer or server). We can have one database working on multiple nodes. Scaling out (or back in) means we can easily add and remove nodes. This makes NoSQL a perfect match for the cloud. Because it can scale out, you will be maximizing the scalability benefits of the cloud. You can run SQL on Azure, for example, but you will be limited in your ability to scale.


We helped our clients create their impact in different industries. Check out our case studies!
Case Studies
NoSQL vs. SQL Speed (of your team)

The ability to store huge amounts of data in a flexible way makes NoSQL faster to develop. You can:

Create a database without a detailed database model Store all different types of data without defining the type of data in advance Add new data types without having to redefine the schema NoSQL pairs well with fast paced, agile development teams. It allows for rapid changes to the database schema as the scope evolves and requirements change.



Again, this doesn’t mean SQL is slow. If your data is highly structured and you anticipate minimal change then there’s probably no reason to use NoSQL. Because SQL is mature and supported by a strong technical community, your engineers won’t run into problems they can’t solve. With NoSQL you’re more likely to run into tough problems without documented solutions which can lead to delays. NoSQL databases also lack standardization. For example, both MongoDB and Cassandra DB are both good NoSQL databases for an engineer new to NoSQL, to learn. However, if an engineer first learns MongoDB, they may still struggle with Cassandra DB because NoSQL lacks standards.




Similarly, SQL is known for its robust features and tools. NoSQL frameworks provide tools to monitor, backup, and maintain NoSQL databases. To date SQL is still stronger. However, as NoSQL matures, more and more features are available. Here are some examples:

Both SQL and NoSQL offer high availability and auto-replication (automatically communicating with another instance when one goes down), but SQL requires configuration while many NoSQL databases automatically include these features.
If you’re working with a multi-tenant application, you will need sharding and partitioning (separating very large databases into smaller, faster, more easily managed parts). To achieve this with SQL databases requires additional coding. NoSQL databases (such as CosmosDB) includes these features out-of-box.




Our Services
Looking for a software service? Check out what we can offer you!
When to use SQL instead of NoSQL

01

You’re working with complex queries and reports.

With SQL you can build one script that retrieves and presents your data. NoSQL doesn’t support relations between data types. Running queries in NoSQL is doable, but much slower.

02

You have a high transaction application.

SQL databases are a better fit for heavy duty or complex transactions because it’s more stable and ensure data integrity.

03

You need to ensure ACID compliance.

(Atomicity, Consistency, Isolation, Durability) or defining exactly how transactions interact with a database. 

04

You don’t anticipate a lot of changes or growth.

If you’re not working with a large volume of data or many data types, NoSQL would be overkill.

When to use NoSQL instead of SQL

01

You are constantly adding new features, functions, data types.

It’s difficult to predict how the application will grow over time.

02

Changing a data model is SQL is clunky and requires code changes.

A lot of time is invested designing the data model because changes will impact all or most of the layers in the application.

03

In NoSQL, we are working with a highly flexible schema design or no predefined schema.

The data modeling process is iterative and adaptive. Changing the structure or schema will not impact development cycles or create any downtime for the application.

04

You are not concerned about data consistency and 100% data integrity is not your top goal.

This is related to the above SQL requirement for ACID compliance. For example, with social media platforms, it isn’t important if everyone sees your new post at the exact same time, which means data consistency is not a priority.

05

You have a lot of data, many different data types, and your data needs will only grow over time.

NoSQL makes it easy to store all different types of data together and without having to invest time into defining what type of data you’re storing in advance.

06

Your data needs scale up, out, and down.

As discussed above, NoSQL provides much greater flexibility and the ability to control costs as your data needs change.

When to Use Both SQL and NoSQL

In answering SQL vs. NoSQL, we have to start with understanding the domain. What’s the end state you’re trying to achieve? SQL vs. NoSQL in 2018 is often not about one or the other, but about when and where to use each within the same application and ecosystem.


We recently designed an application where NoSQL made the most sense for many different reasons. This same application required reports. Instead of overanalyzing the differences between SQL and NoSQL, we decided to use both – NoSQL for the web and desktop versions of the application and SQL for the reports. We plan to store the data in NoSQL databases then transfer only the data we need for reports to a SQL database. If you’re interested, we explain how we proactively designed a ready-to-scale architecture without bloating the application in another blog.


Set up your free technical consultation and find out how we'll bring our vision, mission, and values to successfully execute your next project. 
Contact Us
So, which database is right for your application and team?

There is a lot to navigate and consider. Here, we explored the questions we ask first. We then go deeper into more areas such as which type of NoSQL database to choose, which NoSQL framework is the best and why, how and when to port existing SQL to NoSQL, how to conduct a cost comparison, how to support developers, and how to avoid common pitfalls.



NoSQL is evolving and it’s a bit of the “wild west” out there with options changing quickly. If you’re uncertain when to use SQL vs. NoSQL or which way to go or are facing a tough problem, contact us for a consultation.
