const port: number = 17173
import { app } from "electron"
import child_process from "child_process"

let instance: child_process.ChildProcess

/**
 * 开启python的api服务
 * @returns
 */
export function startServer() {
  judgeServerOpen(17173).then(res => {
    if (!res) {
      console.log("17173 is in used")
      // return
    }
    if (app.isPackaged || process.env["DEBUG"]) {
      instance = child_process.spawn(`main.exe`)
    }
    if (process.platform == "win32") {
      // TODO 启动python api 待改进 后续添加端口占用判断等
      instance = child_process.spawn(`python`, [`${__dirname}/../../api/main.py`, `${port}`])
    } else {
      instance = child_process.spawn("python3", [`${__dirname}/../../api/main.py`, `${port}`])
    }
    if (instance) {
      console.log("server started.")
      instance.stdout?.pipe(process.stdout)
      instance.stderr?.pipe(process.stderr)
      instance.stdin?.pipe(process.stdin)
    }
  })
}

/**
 * 判断端口是否被占用
 * @param port 端口号
 * @returns 该端口是否被占用
 */
function judgeServerOpen(port: number): Promise<boolean> {
  let order = `netstat -ano|findstr "${port}"`
  return new Promise((resolve, reject) => {
    child_process.exec(order, function (error: any, stdout: any, stderr: any) {
      if (stdout === "") {
        resolve(false)
      } else {
        resolve(true)
      }
    })
  })
}

/**
 * 关闭python的api服务
 * @returns
 */
export function stopServer() {
  // TODO 关闭python api
  if (instance) {
    instance.kill(0) && console.log("server stoped.")
  }
  if (process.platform == "win32") {
    child_process.exec("taskkill /f /im python.exe")
    child_process.exec("taskkill /f /im main.exe")
  } else {
    child_process.exec("killall Python")
  }
}
