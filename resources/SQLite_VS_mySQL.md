MySQL vs. SQLite
Exploring the differences between two popular databases.

Photo by Javardh on Unsplash
![image](https://user-images.githubusercontent.com/56029669/196254061-cd54a103-1040-476d-9080-603de59e9f26.png)

As a change of pace, I decided to take a trip back to Databases. This time though, I wanted to do a little comparison instead of another tutorial-style post. Thinking about my time in college, I remember a particular class where we discussed using either MySQL or SQLite. In the end, we used SQLite due to the portability, but this got me thinking. The conversation would suggest that MySQL and SQLite were very similar, however, I know that is not the case. So how are they different? And are there any areas they are very similar? So in this post, we will be discussing just that. How different are MySQL and SQLite? And which is better to use for your project?

A Quick Look At Comparisons
Both MySQL and SQLite are forms of a Relational Database Management System (RDBMS). These are based on the Structured Query Language (SQL). In addition, the syntax of each can be similar, and, in my opinion, it is not too difficult to learn one after the other. That being said, even though this may sound like a very similar background, this is where our similarities end.

A Look At The Background Details
First, to get a start we should look at the background code for each. For both MySQL and SQLite, C is used as the development language. That being said, only MySQL was also developed using C++. Both are also open-sourced. While MySQL is managed by Oracle, SQLite’s code is available for both personal and commercial use in the public domain.

Next, we can take a look at how it runs or what it runs on. MySQL uses a database server to run on a network, which can then be accessed by the client. SQLite, however, is what is known as an embedded database. This means that the structure is stored on the application itself. By storing on the application, SQLite is portable and easy to move, as all table information is located in the file. That being said, it also means that no other application on a network has access to the database.

Being SQLite is portable, it must then also be very lightweight. In fact, the required space, although depending on the system, can be less than 600 KiB. SQLite also requires no prior installation nor setup. Additionally, it is also entirely self-contained and therefore has no external dependencies. SQLite is also sometimes referred to as an “out-of-the-box” RDBMS, as it does not require configuration such as starting or stopping the program. MySQL, on the other hand, does require installation. It also runs much heavier. The required space to function is around 600 Mb. That being said, MySQL also supports replication and scalability.

But What About Datatypes?
Supported datatypes is a large difference between MySQL and SQLite. MySQL supports a wide variety of data types, including different numeric types, date and time types, and string types. This allows for most data to be stored safely inside the correct type if selected well. On the other hand, SQLite does not support nearly as many types. In fact, SQLite supports only NULL, integer, real, text, and blob. As you can see, data may not always find the best fit within one of these types. Such a setback is required to keep SQLite so beginner-friendly and lightweight.

Scalability And Other Important Features
As already touched on earlier, connectivity in a network is one difference between MySQL and SQLite. With SQLite being self-contained, other clients on a network would not have access to the database unlike with MySQL. This is also extended to multi-user capabilities. MySQL is able to handle many connections at the same time. However, SQLite is only able to handle one connection. In addition, with MySQL, different users may be created with a range of different permissions, while with SQLite user management is not a capability and therefore not supported.

In terms of scalability, there are a few different factors to consider. First, MySQL is able to handle a large volume of data. This could be in having a large variety of tables, or it could be having many entries for each table. With SQLite, it is built to run lightweight and small, and so the more data is stored the less efficient and the worse performance is. One small feature that MySQL contains that SQLite does not is the support of XML format. Another very large factor is the matter of authentication. With MySQL, users with permissions may be created, which means those users need to be authenticated. One such form would be usernames and passwords. This is to prevent outside users from being able to either alter or access any information within the database. In SQLite, however, there is no built-in authentication that is supported. This means that not only can anyone access the database, but that entries or even entire tables may be added, updated, or removed by anyone.

Although multi-user accessibility may not be supported by SQLite, there is some very limited concurrency. This means that multiple processes are able to access the database at the same time, but making changes at the same time is not something supported. However, with MySQL concurrency is much more possible. That being said, making changes at the same time could still pose issues, which would make these issues in RDBMS similar.

Security is a large, and important, feature of MySQL. Because it is server-side, MySQL has built-in features to keep unwanted people from easily accessing data. Although not perfect, it provides a world of difference when compared to SQLite. This is because SQLite is embedded, and therefore does not have the same bug prevention other important security features that MySQL has as a server-side database.

How And When To Choose
In large, MySQL is used when transactions are more frequent. It is commonly used on web and desktop applications. MySQL should also be selected if network capabilities are a must. It would also be the choice if multiple users are needed, if stronger security is required, or if authentication is involved. If a large amount of data is needed to be stored, MySQL would also be the choice for the job.

SQLite is more commonly used when data is predefined and used on applications such as on mobile. For such applications, being confined in the files of the device is not a problem, and a network is not needed. That being said, there are times where SQLite may be the choice. Such a time is if a small amount of space remains, or if small amounts of data need to be stored for an application that will minimally access the database and not require heavy calculations. I know when I was making small projects in college, SQLite was a good way to get a database created quickly. Those little stand-alone applications may not need users, or even the ability for more than the application to reach the database, which is when SQLite may be the decision for you.

All-in-all, it really comes down to what you’re comfortable using, and what you think seems like the better fit. After all, no one will know your project as well as you do.

Conclusion
As a change of pace, I thought comparing two different RDBMS, MySQL and SQLite, was an interesting dive. It gave not only a little background on each but more of an understanding of how each worked. We also looked at a few major differences between the two, and that they really are less similar than what you may be lead to believe. In the end, we took a short look at when you may want to use one over the other, although that is more up to the user and your particular project. I hope you learned something from this, and that you found the information useful. I know I found it interesting. Until next time, cheers!

Read all my articles for free with my weekly newsletter, thanks!

Want to read all articles on Medium? Become a Medium member today!

