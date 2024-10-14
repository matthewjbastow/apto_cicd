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
        stage('read') {
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
        stage('run') {
                    steps {
                        sh 'echo "Running script..."'
                        sh '''
                            echo "going to run script now"
                            pwd
                        '''
                        sh 'ls -l'
                        sh 'chmod +x test.sh'
                        sh './test.sh'
            }
        }
    }
}
