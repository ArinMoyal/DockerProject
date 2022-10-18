pipeline {
  agent any
  stages {
    stage('Check AlpCon Status') {
      steps {
        sh '''
                if [ "$( docker container inspect -f '{{.State.Status}}' AlpCon )" == "running" ]; then
                        echo "AlpCon is already running. Skipping all stages."
                        env.RUN = 1
                else
                        echo "AlpCon not running, starting AlpCon"
                        env.RUN = 0
                fi
          '''
//        env.RUN = 0
        }
      }
    stage('Running Python Script') {
//      when {
//        expression {
//                env.RUN == 0
      steps {
        script {
                    env.SUCCESS = 1
                    try {
                        timeout(time: 10, unit: 'SECONDS') {
                        sh 'docker run -v ${WORKSPACE}/cubecalculation:/cubecalculation --name AlpCon alpcon'
                        }
                    } catch (err) {
                        env.SUCCESS = 0
                    }
                }
          }
      }
      stage('TimedOut') {
        when {
            expression {
                env.SUCCESS == 0
            }
        }
        steps {
            sh  '''
                    echo "Script timed-out. Try lowering the range of numbers."
                    docker stop AlpCon
                '''
        }
  }
      stage('Success') {
        when {
            expression {
                env.SUCCESS == 1
                }
            }
            steps {
                sh  '''
                        echo "Script succeeded! Results have been logged at ${WORKSPACE}/results."
                        docker stop AlpCon
                    '''
            }
        }
 }
}
