pipeline {
    
    agent {node { label 'slave1' }}

    stages {
        stage('Hello') {
          agent {
            docker {
              label 'slave1'
              image 'ubuntu'
            }
           }

            steps {
                echo 'Hello World'
            }
        }
    }
}
