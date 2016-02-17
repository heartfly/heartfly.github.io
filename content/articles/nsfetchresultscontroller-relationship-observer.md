Title: NSFetchResultsController如何监听relationship的变化？
Date: 2014-6-24 12:06
Category: iOS
tags: Core Data, NSFetchResultsController, relationship
Slug: nsfetchresultscontroller-relationship-observer
Author: qxh
Summary: 我们知道,当CoreData表中的attribute改变时,使用NSFetchedResultsController可以通知UITableView做出实时的改变.那如果像下图中relationship对象的attribute改变时,如何实现这样的通知呢？

我们知道,当CoreData表中的attribute改变时,使用NSFetchedResultsController可以通知UITableView做出实时的改变。
 
那如果像下图中relationship对象的attribute改变时,如何实现这样的通知呢？
  
![Core Data Relationship](/images/coredata_relationship.png)

* 需要在attribute修改成功后发送如下消息：

    [contact willChangeValueForKey:@"grp"];
    [contact didChangeValueForKey:@"grp"];



