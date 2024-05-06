pipeline {
     agent any
     
     stages {
        stage('Build') {
            steps {
               echo " Hello World"
                    //python setup.py build // Build the project
                }
            }
     }
          post{
               always{
                    cleanWs()
               }
          }
        }    
    
