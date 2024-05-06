pipeline {
     agent any
     
     stages {
          stage('Compile') {
            steps {
               echo "Compilation Successful"
                    //python setup.py build // Build the project
                }
            }
        stage('Build') {
            steps {
               echo " Build Successful "
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
    
