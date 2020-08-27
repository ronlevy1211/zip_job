podTemplate(label: 'mypod', containers: [
    containerTemplate(name: 'zip_job', image: 'ronlevy1211/zip_job', ttyEnabled: true, command: '/bin/bash -c')
  ]
  ) 
node {
    stage('Start Zip Build'){
        container('zip_job'){
            sh """
                python3 zip_job.py
            """
        }
    }
} 