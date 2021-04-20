初始化数据库
```sql
create user 'aweffr_com'@'%' identified by '***********';
create database aweffr_com character set utf8mb4 collate utf8mb4_unicode_ci;
grant all privileges on aweffr_com.* to 'aweffr_com'@'%';
```


migrate之前要patch
`https://github.com/wagtail/wagtail/pull/6999/files`

wagtail 2.12.3 有一个migrate的bug
