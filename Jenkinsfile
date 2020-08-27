podTemplate(label: 'zipjob', containers: [
    containerTemplate(name: 'zipjob', image: 'ronlevy1211/zip_job', ttyEnabled: true, command: '/bin/bash -c'),]
  )
node('zipjob') {
    stage('Start Zip Build'){
        container('zipjob'){
            sh """
                python3 zip_job.py
            """
        }
    }
} 