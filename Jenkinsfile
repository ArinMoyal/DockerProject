pipeline {
  agent any
  stages {
    stage('Check AlpCon Status') {
      steps {
        sh '''
                if [ "$( docker container inspect -f '{{.State.Status}}' AlpCon )" == "running" ]; then
                        echo "AlpCon is already running."
                        RUN=false
                else
                        echo "AlpCon not running, starting AlpCon"
                        RUN=true
                fi
           '''
      }
    }
    stage('Running Python Script') {
//      when {
//        expression {
//                return RUN
//       }
//    }
      steps {
        timeout(time: 10, unit: 'SECONDS') {
          sh 'docker run -v /cubecalculation:/cubecalculation --name AlpCon alpcon'
    }
   }
  }
 }
}
