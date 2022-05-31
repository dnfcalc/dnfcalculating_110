import api from "@/api"
import { useDialog } from "@/components/hooks/dialog"
import openURL from "./openURL"
const { show } = useDialog()

export async function checkUpdate() {
  if (window.ipcRenderer && process.env.NODE_ENV !== "development") {
    const version = await window.ipcRenderer.invoke("getVersion")
    api
      .checkUpdate(version)
      .then(async res => {
        if (res) {
          show({
            content: () => (
              <>
                <div class="w-full justify-center text-left">
                  检测到更新，是否自动更新？
                  <br />
                  自动更新后台静默下载，下次启动时生效。
                </div>
              </>
            ),
            rejectButton: "手动更新",
            okButton: "自动更新",
            cancelButton: "取消"
          }).then(res => {
            console.log(res.status)
            if (res.status == "reject") {
              openURL("https://wwn.lanzout.com/s/dcalc")
            }
            if (res.status == "ok") {
              api.autoUpdate()
            }
          })
        }
      })
      .catch(async ex => {
        await alert({
          content: "自动检查更新错误,请手动检查更新"
        })
      })
  }
}
