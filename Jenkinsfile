pipeline {
    agent any
        environment {
        SPLUNK_APP_DIR = "TA-sample-app"
        APP_PACKAGE = "TA-sample-app.tar.gz"
        SPLUNK_CREDENTIALS = credentials('SPLUNK_CREDENTIALS') // ACS Username
        SPLUNK_CLOUD_API_URL = "https://api.splunk.com/2.0/rest/login/splunk"
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building..."'
                echo "Username: ${SPLUNK_CREDENTIALS_USR}"
                echo "Password: ${SPLUNK_CREDENTIALS_PSW}"
            }
        }
        stage('Package Splunk App') {
            steps {
                echo "Packaging the Splunk app"
                echo "Cleaning DS_store Files"
                sh 'find $SPLUNK_APP_DIR -name ".DS_Store" -type f -delete'
                sh 'python3 scripts/package_splunk_app.py ${SPLUNK_APP_DIR} ${APP_PACKAGE}'
            }
        }
        stage('Get ACS Token') {
            steps {
                script {
                    echo "Retrieving ACS token"
                    def jwt_token = sh(script: 'python3 scripts/get_jwt_token.py ${ACS_USERNAME} ${ACS_PASSWORD}', returnStdout: true).trim()
                    // Store the token as an environment variable for later stages
                    env.JWT_TOKEN = jwt_token
                    echo "JWT Token retrieved and stored"
                    echo "$JWT_TOKEN"
                }
            }
        }
        stage('Submit to AppInspect API') {
            steps {
                echo "Submitting the app to Splunk AppInspect API"
                sh 'python3 scripts/inspect_splunk_app_api.py ${APP_PACKAGE} ${JWT_TOKEN}'
            }
        }
    }
}
