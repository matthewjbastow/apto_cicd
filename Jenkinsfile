pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
                sh '''
                    echo "going to deploy here"
                    pwd
                    chmod -x test.sh
                '''
                sh 'ls -la'
            }
        }
    }
}
