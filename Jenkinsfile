pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building..."'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
                sh '''
                    echo "going to deploy here"
                    pwd
                    chmod 777 test.sh
                '''
                sh 'ls -la'
                sh './test.sh'
            }
        }
    }
}
