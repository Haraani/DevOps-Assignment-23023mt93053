pipeline {
     agent any
     stages {
        
        stage('Build') {
            steps {
                script{
                    echo " Hello World"
                    python setup.py build // Build the project
                }
            }
        }    
    }
}
