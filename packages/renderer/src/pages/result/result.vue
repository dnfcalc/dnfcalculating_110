<script lang="tsx">
  import { getSession } from "@/utils"
  import { defineComponent, ref } from "vue"
  import { useRoute } from "vue-router"
  import api from "@/api"

  export default defineComponent(async () => {
    const uid = (useRoute().query.uid as string) ?? ""
    let saveData: any = await getSession(uid)
    return () => (
      <>
        <div>{JSON.stringify(saveData)}</div>
      </>
    )
  })
</script>
