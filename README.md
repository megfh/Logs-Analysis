# Logs Analysis

This project is being completed as one of the requirements for Udacity's Full Stack Nanodegree

The project is a reporting tool for the database of a newspaper site that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

The project uses the Python Standard Library (Python 2.7.10).

### Installation and Setup

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2. Fork the [fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)
3. Clone your fullstack-nanodegree-vm repository to your local machine
4. Download logs.py to the fullstack-nanodegree-vm/vagrant directory
5. Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) (you will need to unzip this file after downloading it)
6. Move newsdata.sql to the vagrant directory

### Launch the VM

1. Navigate to the full-stack-nanodegree-vm/vagrant directory in terminal
2. Use command **vagrant up** to power on the VM
3. Use command **vagrant ssh** to log into the VM
4. Use command **cd/vagrant** to change to the vagrant directory
5. Use command **psql -d news -f newsdata.sql** to load the data
6. Create the necessary views:
    - Use command **psql -d news** to connect to the database
    - execute **create view** statements listed below
    - Use command **\q** to exit the psql CLI
7. Use command **python logs.py** to run the program

Note: The Vagrant VM provided in the fullstack repo already has PostgreSQL server and psql CLI installed.

Several views were added to the database in building this tool. The commands to recreate those views are listed below:

 - 'create view ArticleCount as select articles.title, count(path) from log inner join articles on substr(log.path,10)=articles.slug where status='200 OK' and path<>'/' group by articles.title order by count desc;'

 - 'create view authorsWork as select articles.title, authors.name from articles inner join authors on articles.author=authors.id;'

 - 'create view errors as select * from log where status<>'200 OK';'

 - 'create view numErrors as select date_trunc('day', time), count(*) from errors group by date_trunc('day', time);'

 - 'create view numRequests as select date_trunc('day', time), count(*) from log group by date_trunc('day', time);'

 - 'create view daily_requests as select numRequests.date_trunc, numRequests.count as total_requests, numErrors.count as total_errors from numErrors inner join numRequests on numRequests.date_trunc=numErrors.date_trunc;'

 - 'create view percentError as select date_part('month', date_trunc) as "month", date_part('day', date_trunc) as "day", date_part('year', date_trunc) as "year", cast(total_errors as float)/cast(total_requests as float)*100 as "percent_error" from daily_requests;'
