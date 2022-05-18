<script lang="tsx">
  import { getSession } from "@/utils"
  import { defineComponent, ref } from "vue"
  import { useRoute } from "vue-router"
  import api from "@/api"

  export default defineComponent(async () => {
    const uid = (useRoute().query.uid as string) ?? ""
    let data: any = undefined
    window.ipcRenderer.invoke("getStorage", "1234").then(res => console.log(res))
    return () => (
      <>
        <div>{data}</div>
      </>
    )
  })
</script>
