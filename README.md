Overview of the Project:

    For this project, a basic machine learning application is developed, containerized using Docker, and released on GitHub. The container environment is defined by a Dockerfile containing a Flask web application that serves a machine learning model which was trained using a decision tree classifier on the Iris dataset. An endpoint for generating predictions based on input data is provided by the application. 


Instructions for build & run docker container as well as testing of ML endpoints

    Step-1 we have skipped this step as we have use windows to run docker instead of Virtual machines

    step-2 install docker
    - we have downloaded docker desktop in windows through google
    - signed in with username & password

    step-3 create Dockerfile for ML application

        part 1 create project directory
        - we have created directory named 'ml-app' using 'mkdir ml-app' command

        part 2 create dockerfile
        - created file using vscode (visual studio code )

        part 3 create requirement.txt
        - created in notepad

    step-4 developing machine learning application

        part 1 creating simple model
        - created using vscode

        part 2 run the model
        - ran the model in vscode

        part 3 integrate model with flask
        - created flask model in vscode & predict the result

        part 4 update the product directory
        - saved all the above files at one location using file explorer


    step-5 build & run docker container

        part 1 build docker image
        - build the image on vscode

        part 2 run docker container
        - ran the docker through vscode

        part 3 access the application
        - opened the browser & load the application

        part 4 test the ML endpoint
        - predicted value of iris classification using given input data points by using thunder client


    step-6 deploy to Github

        part 1 initialize git repository
        - initialize the git repository in github desktop

        part 2 add files & commit
        - added all the above given docker files & model files

        part 3 create new repository
        - pushed the local repository

Some extra information:

    Docker: It is an open-sourse platform used to automate deployment of application using containers. Containers are software packages that includes code, libraries & dependencies.

    Thunder Client: It is a lightweight REST API. It is designed to debug APIs in the vscode environment. We have used thunder client to send POST request with input data.

    GitHub: It is a platform providing version control & software development services. We can create software projects & publish it in public.






