<script lang="tsx">
  import { defineComponent, ref, renderList } from "vue"
  import api from "@/api"
  import { useDialog } from "@/components/hooks/dialog"
  export default defineComponent(async () => {
    const globalSet = await api.getGlobalSet().then(r => r)
    const details = ref(globalSet.detail as number[])
    const { alert } = useDialog()
    for (let i = 0; i < globalSet.info.length - details.value.length; i++) details.value.push(0)

    function set() {
      return () => {
        api.saveGlobalSet(details.value).then(res => {
          alert({
            content: "保存成功"
          })
        })
      }
    }
    return () => (
      <div
        class="bg-cover bg-no-repeat h-100% pt-8 pb-8 pl-4 pr-4 flex flex-col justify-between"
        style="background-image: url('/images/adventure/bg.jpg');max-height: calc(100% - 4rem);background-size: 100% 100%;"
      >
        <div class="flex flex-col set">
          {renderList(globalSet.info, (set, index) => (
            <>
              <div class="item">
                {index + 1}.{set.remark}
                <div class="ml-10px flex items-center">
                  <div class="w-100px">{set.name}</div>
                  <calc-select class="!h-20px !ml-10px" v-model={details.value[index]}>
                    {renderList(set.items, item => (
                      <calc-option value={item.value}>{item.label}</calc-option>
                    ))}
                  </calc-select>
                </div>
              </div>
            </>
          ))}
        </div>
        <div class="h-2rem w-100% flex justify-center items-center">
          <calc-button onClick={set()}>保存</calc-button>
        </div>
      </div>
    )
  })
</script>
<style lang="scss">
  .set {
    color: rgba(190, 163, 71, 1);
    overflow-y: auto;
    .item {
      display: flex;
      padding-left: 20px;
      flex-direction: column;
      line-height: 30px;
    }
  }
</style>
