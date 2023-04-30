# fontys-spring2023-microservices-messaging-kafka
Workshop resources for the Fontys Spring 2023 workshop on microservices, messaging and Apache Kafka

This workspace comes with Apache Kafka (Docker Compose with 3-brokers, Zookeeper, AQ HK, Schema Registry and REST Proxy) and Java, Go, Node and Python runtimes as well as Maven, Pip, NPM and other build tools).

A multi part hands on guide is available with many code samples and examples of how to interact with Kafka from various technologies. These are the labs:

* [Getting started with Apache Kafka](./lab1-firstStepsWithKafka/readme.md)
* [Introduction to Node the programming language](./lab2-introducingNodeJS/readme.md)
* [Working with Apache Kafka from Node programs](./lab3-node-and-kafka/readme.md)
* [Do It Yourself CQRS with Apache Kafka and Node](./lab4-diy-cqrs/readme.md)
* [Kafka from Python](./lab5-python-and-kafka/readme.md)
* [Kafka from Java](./lab6-java-and-kafka/readme.md)
* [Kafka from Go](./lab7-go-and-kafka/readme.md)


[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/lucasjellema/fontys-spring2023-microservices-messaging-kafka)

By clicking this button, you will launch a Gitpod workspace - associated with your Github account. This is free. At the time of writing, the first 50 hours each month (yes, *50 hours* again *each month*) of workspace usage are free. This workspace comes with VS Code in the browser, the language runtimes and build tools as well as Docker and Docker Compose. Once running, the workspace is initialized from the GitHub repo with all sources and this README document, Docker Compose is started to launch the containers for the Apache Kafka Cluster and supporting tooling.

## Working in your local VS Code (against the Gitpod workspace)
If you prefer to work with your local desktop version of VS Code instead of VS Code in the browser or you like to access one of the services and ports running in the Gitpod workspace from your own laptop, you can certainly do so. Try to open a workspace in your local VS Code desktop for the smoothest dev experience (using port forwarding for services and web applications). 
![image](https://user-images.githubusercontent.com/1296324/202265821-1faa9cc3-21fa-4cc2-8add-163ec5b83e9b.png)

You need the MS Remote SSH extension for VS Code:
![image](https://user-images.githubusercontent.com/1296324/202265701-ffe9492d-ff60-40e7-96c5-203d1ecedb70.png)

Also install the VS Code extension Gitpod Remote
![image](https://user-images.githubusercontent.com/1296324/202265866-5ac13ef4-3db9-4f2f-9c42-ca6ab900dcc6.png)

Open the command palette in VS Code in the browser. Select Gitpod - Open in VS Code.
![image](https://user-images.githubusercontent.com/1296324/202265911-37a26892-3d50-4258-95bc-d8cfc18d537c.png)

You will be asked:
* Open Visual Studio Code?
* Copy the this temporary password
* Allow an extension to open this URL?
* Enter password for remote connection

as shown in this picture.
![image](https://user-images.githubusercontent.com/1296324/202266010-244eeff3-1a53-4d4d-a997-64eb159f8c0a.png)

Please comply and provide as requested.

You can now work locally against the CDE (Cloud Development Environment) - the cloud based Gitpod workspace environment. Try to type in the local editor and quickly check the browser based editor - and vice versa. Be really quick! They seem pretty well synchronized.

Note: If you run a web application or a service that opens ports, you may want to forward ports - make sure that attempts to access localhost:SOME_PORT are forwarded correctly over the SSH connection to the Gitpod workspace environment.

![image](https://user-images.githubusercontent.com/1296324/202266756-39b4b3cb-dbd8-4b9e-b4ee-a8e8450a29d6.png)


## Collaborating in your Workspace

You can invite othes to come and join you in your workspace. It is similar to collaborating on Google Docs, in that you can see who is online and look at the same code and processes. It is like others working on your machine at the same time as you. You do not actually live share an editor though. 

See: [Gitpod Docs on Sharing a running Workspace](https://www.gitpod.io/docs/configure/workspaces/collaboration#sharing-running-workspaces).

Now invite a colleague to visit your place - and get a feel for working together.

## Workspace Snapshots

A snapshot of a workspace is the workspace with all its files in all directories - the result of all your manual steps. A snapshot can restore a workspace in that exact same state (including files that were not committed to git and/or were installed outside of the /workspace directory. A URL can be retrieved for a snapshot - and that URL can be shared with others. Snapshotting a workspace is useful when you want to create reproducible workspace state for reporting support issues, or when giving training, or presentations. You can create up to three snapshots from any workspace.

Note: a snapshot does not have any running processes (besides what is defined in tasks to run for workspace restart).

See [Gitpod Docs on Snapshots of Workspaces](https://www.gitpod.io/docs/configure/workspaces/collaboration#sharing-snapshots).

Create one or two files in this workspace. Change one of the files already there. Do not commit any file. Now create a snapshot:

Run "Gitpod: Share Workspace Snapshot" from the hamburger menu at the top left of VS Code, from the Gitpod menu at the bottom, or via the VS Code command palette. Once you execute the command, the snapshot is taken and the URL is shown in a dialog.

Share the URL with a colleague, ask them to open the URL and verify that see the workspace as you defined it. Alternatively or additionally, open a new browser window and navigate to the snapshot URL. Check that you see the exact same situation as in the original workspace.

Note: the snapshots are a capture of a specific point in time. From this point on, the workspace forks from the snapshot. Changes in the workspace will not affect the snapshot. Any workspace opened from the snapshot is also a clone from the snapshot that is immediately cut loose from it.
