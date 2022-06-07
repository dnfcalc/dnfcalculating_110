import { app, BrowserWindow, shell, ipcMain } from "electron"
import { release } from "os"
import { join } from "path"
import { startServer, stopServer } from "./server"

// Disable GPU Acceleration for Windows 7
if (release().startsWith("6.1")) app.disableHardwareAcceleration()

// Set application name for Windows 10+ notifications
if (process.platform === "win32") app.setAppUserModelId(app.getName())

process.env["ELECTRON_DISABLE_SECURITY_WARNINGS"] = "true"

if (!app.requestSingleInstanceLock()) {
  app.quit()
  process.exit(0)
}

let win: BrowserWindow | null = null

let storage = {}

async function createWindow() {
  win = new BrowserWindow({
    frame: false,
    width: 861,
    height: 680,
    resizable: false,
    icon: join(__dirname, "./favicon.ico"),
    webPreferences: {
      preload: join(__dirname, "../preload/index.cjs"),
      nodeIntegration: true,
      contextIsolation: false,
      webSecurity: false
    }
  })
  win.setMenuBarVisibility(false)

  if (app.isPackaged) {
    win.loadFile(join(__dirname, "../renderer/index.html"))
  } else {
    // 🚧 Use ['ENV_NAME'] avoid vite:define plugin
    const url = `http://${process.env["VITE_DEV_SERVER_HOST"]}:${process.env["VITE_DEV_SERVER_PORT"]}`
    win.loadURL(url)
    win.webContents.openDevTools({ mode: "undocked", activate: true })
  }

  // Test active push message to Renderer-process
  win.webContents.on("did-finish-load", () => {
    win?.webContents.send("main-process-message", new Date().toLocaleString())
  })

  // Make all links open with the browser, not with the application
  win.webContents.setWindowOpenHandler(({ url }) => {
    if (url.startsWith("https:")) shell.openExternal(url)
    return { action: "deny" }
  })

  win.setMenuBarVisibility(false)
}

startServer()

setTimeout(() => {
  app.whenReady().then(createWindow)
}, 5000)

app.on("window-all-closed", () => {
  win = null
  app.quit()
})

app.on("quit", () => {
  console.log("app quit.")
  stopServer()
  app.exit(0)
})

app.on("second-instance", () => {
  if (win) {
    // Focus on the main window if the user tried to open another
    if (win.isMinimized()) win.restore()
    win.focus()
  }
})

app.on("activate", () => {
  const allWindows = BrowserWindow.getAllWindows()
  if (allWindows.length) {
    allWindows[0].focus()
  } else {
    createWindow()
  }
})

ipcMain.handle("open-win", (event, arg) => {
  const childWindow = new BrowserWindow({
    width: arg.width,
    height: arg.height,
    resizable: false,
    frame: false,
    icon: join(__dirname, "./favicon.ico"),
    webPreferences: {
      preload: join(__dirname, "../preload/index.cjs"),
      webSecurity: false,
      nodeIntegration: true,
      contextIsolation: false
    }
  })

  if (app.isPackaged) {
    childWindow.loadFile(join(__dirname, `../renderer/index.html`), {
      hash: `${arg.url}`
    })
  } else {
    // 🚧 Use ['ENV_NAME'] avoid vite:define plugin
    const url = arg.url
    childWindow.loadURL(url)
  }
})

ipcMain.handle("minimize-win", event => {
  const window = BrowserWindow.fromWebContents(event.sender)
  if (window) {
    window.minimize()
  }
})

ipcMain.handle("close-win", event => {
  const window = BrowserWindow.fromWebContents(event.sender)
  if (window) {
    window.close()
  }
})

ipcMain.handle("getStorage", (event, arg) => {
  return storage[arg] ?? undefined
})

ipcMain.handle("getVersion", (event, arg) => {
  return app.getVersion()
})

ipcMain.handle("setStorage", (event, arg) => {
  Object.defineProperty(storage, arg.key, {
    value: arg.value,
    writable: true,
    enumerable: true,
    configurable: true
  })
})

process.on("exit", () => {
  app.quit()
})
