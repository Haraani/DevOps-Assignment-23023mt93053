pipeline {
     agent any
     tools {
          maven 'Maven 3.9.6'
          jdk 'jdk8'
     }
     stages {
          stage ('Initialize') {
            steps {
                sh '''
                    echo "PATH = ${PATH}"
                    echo "M2_HOME = ${M2_HOME}"
                ''' 
            }
        }
        stage('Build') {
            steps {
               echo " Hello World"
                    //python setup.py build // Build the project
                }
            }
        }    
    }
