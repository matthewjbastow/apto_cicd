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
                sh 'echo "Reading..."'
                sh '''
                    echo "going to read file now"
                    pwd
                '''
                sh 'ls -l'
                sh 'cat test.txt'
            }
        }
    }
}
