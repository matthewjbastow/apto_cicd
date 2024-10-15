pipeline {
    agent any
        environment {
        SPLUNK_APP_DIR = "TA-sample-app"
        APP_PACKAGE = "TA-sample-app.tar.gz"
        ACS_USERNAME = credentials('matthewbastow') // ACS Username
        ACS_PASSWORD = credentials('JfB9105&') // ACS Password or Token
        SPLUNK_CLOUD_API_URL = "https://api.splunk.com/2.0/rest/login/splunk"
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building..."'
            }
        }
        stage('Package Splunk App') {
            steps {
                echo "Packaging the Splunk app"
                sh 'python3 scripts/package_splunk_app.py ${SPLUNK_APP_DIR} ${APP_PACKAGE}'
            }
        }
        stage('Get ACS Token') {
            steps {
                script {
                    echo "Retrieving ACS token"
                    def acs_token = sh(script: 'python3 scripts/get_acs_token.py ${ACS_USERNAME} ${ACS_PASSWORD} ${SPLUNK_CLOUD_URL}', returnStdout: true).trim()
                    // Store the token as an environment variable for later stages
                    env.ACS_TOKEN = acs_token
                    echo "ACS Token retrieved and stored"
                    echo "$ACS_TOKEN"
                }
            }
        }
    }
}
