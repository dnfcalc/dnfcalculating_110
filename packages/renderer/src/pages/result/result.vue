<script lang="tsx">
  import { getSession, toMap } from "@/utils"
  import { defineComponent, ref } from "vue"
  import { useRoute } from "vue-router"
  import { useCharacterStore, useConfigStore, useAppStore } from "@/store"
  import profile from "@/components/internal/profile.vue"

  export default defineComponent({
    components: { profile },
    async setup() {
      const uid = (useRoute().query.uid as string) ?? ""
      const configStore = useConfigStore()
      const characterStore = useCharacterStore()
      let data: any = await getSession(uid)
      const res = data.res
      configStore.forge_set = (toMap({ forge_set: data.forge_set }) as { forge_set: any }).forge_set
      characterStore.alter = data.alter
      characterStore.name = data.name
      useAppStore().title = "详细数据"

      return () => (
        <>
          <div class="m-0 flex h-100%">
            <div class="h-100% w-280px flex justify-center" style="background-color:black">
              {<profile class="!m-0 !p-0"></profile>}
            </div>
            <div class="w-500px">{JSON.stringify(res)}</div>
          </div>
        </>
      )
    }
  })
</script>
