node {
    stage('Start Zip Build'){
        container('zipjob'){
            sh """
                python3 /tmp/zip_job.py
                echo 'Zip Build completed Successfully!'
            """
        }
    }
}