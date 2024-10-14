pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'echo "Building..."'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
        stage('deploy') {
            steps {
                sh 'echo "Deploying..."'
                sh '''
                    echo "going to run script now"
                    pwd
                '''
                sh './test.sh'
            }
        }
    }
}