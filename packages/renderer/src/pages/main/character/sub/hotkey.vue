<script lang="tsx">
  import { computed, defineComponent, reactive, ref, renderList } from "vue"
  import { useCharacterStore, useConfigStore } from "@/store"
  import { skill_icon } from "./utils"
  export default defineComponent({
    name: "hotkey",
    components: {},
    setup(props, { emit, slots }) {
      const characterStore = useCharacterStore()
      const configStore = useConfigStore()
      // const skillList = computed(() => {
      //   return characterStore.skill_set.filter(item => item.direct)
      // })

      const skillList = computed(() => {
        return (index: number) => {
          return characterStore.skills.filter(skill => skill.type == 1 && configStore.hotkey_set.filter((a, b) => b != index).indexOf(skill.name) < 0)
        }
      })
      return () => (
        <div class="w-240px">
          <div class="mt-2% skill-slots subitem">
            <div class="head-sec">技能快捷键设置</div>
            <div class="body-sec">
              <div class="flex flex-wrap flex-1 w-100% justify-center">
                {renderList(14, item => (
                  <div class="skill-slot-item">
                    <calc-iconselect class="!pt-1px" emptyLabel="点击" columnNum={5} v-model={configStore.hotkey_set[item - 1]}>
                      <calc-option class="bg-hex-000000 h-28px w-28px items-center justify-center !flex" value="">
                        无
                      </calc-option>
                      <calc-option class="bg-hex-000000 h-28px w-28px items-center justify-center !flex" value="其它">
                        其它
                      </calc-option>
                      {renderList(skillList.value(item - 1), skill => (
                        <calc-option value={skill.name}>
                          <div>
                            <img src={skill_icon(characterStore.alter, skill.name)} />
                          </div>
                        </calc-option>
                      ))}
                    </calc-iconselect>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .skill-slot-item {
    height: 32px;
    width: 32px;
    margin-bottom: 10px !important;
    background-color: black;
    border: rgb(29, 29, 29) solid 1px;
    margin: 5px;
  }
</style>
