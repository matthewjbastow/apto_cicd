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
    }
}
