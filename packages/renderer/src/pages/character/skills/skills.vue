<script lang="tsx">
  import { useDialog } from "@/components/hooks/dialog"
  import Draggable from "@/components/vuedraggable/vuedraggable"
  import { useCharacterStore, useConfigStore } from "@/store"
  import { onKeyStroke } from "@vueuse/core"
  import { defineComponent, renderList } from "vue"
  import Cp from "./sub/cp.vue"
  import SkillList from "./sub/list.vue"
  import { skill_icon } from "./sub/utils"

  const upline = ["Q", "W", "E", "R", "T", "Y"]
  const downline = ["A", "S", "D", "F", "G", "H"]
  const keys = [...upline, "Ctrl", ...downline, "Alt"]
  const hotKeys = [...keys, ...upline.concat(downline).map(r => r.toLowerCase()), "Control"]

  export default defineComponent({
    setup() {
      const characterStore = useCharacterStore()
      const configStore = useConfigStore()
      const { confirm } = useDialog()

      const skillList = (index: number) => {
        return characterStore.skills.filter(skill => skill.type == 1 && configStore.hotkey_set.filter((a, b) => b != index).indexOf(skill.name) < 0)
      }

      onKeyStroke(
        hotKeys,
        event => {
          event.preventDefault()
          let { key } = event
          if (key.length == 1) {
            key = key.toUpperCase()
          } else if (key == "Control") {
            key = "Ctrl"
          }
          const index = keys.indexOf(key)
          if (index > -1) {
            const skill_name = configStore.hotkey_set[index]
            console.log(skill_name)
            if (skill_name) {
              const skill = characterStore.skills.find(skill => skill.name == skill_name)
              if (skill) {
                configStore.addSkillQueue(skill)
              }
            }
          }
        },
        {}
      )

      onKeyStroke(
        "Backspace",
        event => {
          event.preventDefault()
          resetQueue()
        },
        {}
      )

      const colors = ["#fee86b", "#75ae1b", "#1bae83", "#1b63ae", "#b920c3", "c3207c"]

      const changeMode = (skill: { name: string; id: number; mode: string; modes: string[] | undefined }) => {
        return () => {
          let index = skill.modes?.indexOf(skill.mode) ?? 0
          console.log(index)
          index = index >= 0 ? (index + 1 >= (skill.modes?.length ?? 0) ? 0 : index + 1) : 0
          skill.mode = skill.modes?.[index] ?? ""
        }
      }

      const item = (item: any, index: number) => {
        const skill = item.element as { name: string; id: number; mode: string; modes: string[] | undefined }
        return (
          <div
            class="h-7 m-2px w-7"
            style={"position: relative;" + (skill.modes?.length ?? 0 > 0 ? (skill.modes?.indexOf(skill.mode) ?? 0 > 0 ? "background-color: " + colors[skill.modes?.indexOf(skill.mode) ?? 0] : 0) : "")}
            onClick={changeMode(skill)}
          >
            <img style={skill.modes?.length ?? 0 > 0 ? (skill.modes?.indexOf(skill.mode) ?? 0 > 0 ? "mix-blend-mode: luminosity;" : "") : ""} src={skill_icon(characterStore.alter, skill.name)} />
            {skill.modes && skill.modes.length > 0 && <div class="size-11">{skill.mode}</div>}
          </div>
          // <div class="list-group-item">{item.element.name}</div>
        )
      }

      async function resetQueue() {
        if (configStore.skill_que.length == 0) {
          return
        }
        const rs = await confirm({ content: "请确认要初始化技能队列吗？" })
        if (rs.isOk) {
          configStore.skill_que.length = 0
        }
      }

      return () => (
        <div class="flex space-x-4 py-2 px-4 character">
          <div class="flex p-1">
            <SkillList></SkillList>
          </div>

          {characterStore.is_delear && (
            <div class="w-70">
              <div class="subitem">
                <div class="head-sec">快捷键</div>
                <div class="py-2 px-1 body-sec ">
                  <div class="flex flex-wrap flex-1 w-full justify-center">
                    {renderList(keys, (item, i) => (
                      <div class="h-7 m-1 w-7 skill-slot-item relative">
                        <calc-iconselect columnNum={5} v-model={configStore.hotkey_set[i]}>
                          <calc-option class="bg-hex-000000 h-28px w-28px items-center justify-center !flex" value=""></calc-option>
                          {renderList(skillList(i), skill => (
                            <calc-option value={skill.name}>
                              <div>
                                <img src={skill_icon(characterStore.alter, skill.name)} />
                              </div>
                            </calc-option>
                          ))}
                        </calc-iconselect>
                        <div class="right-0 bottom-0 absolute">{keys[i]}</div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
              <div class="mt-4 w-full">
                <div class="h-80 skill-slots subitem  overflow-y-auto">
                  <div class="flex px-1 head-sec items-center justify-between">
                    <div class="w-5"></div>
                    <div>技能队列</div>
                    <calc-button onClick={resetQueue} icon="reset" title="初始化(Backspace)"></calc-button>
                  </div>
                  <div class="body-sec">
                    <Draggable class="flex flex-wrap" v-model:list={configStore.skill_que} group={{ name: "people", pull: "clone", put: false }} itemKey="id">
                      {{
                        item
                      }}
                    </Draggable>
                  </div>
                </div>
              </div>
            </div>
          )}
          <div class="w-64">
            <div class="h-220px subitem">
              <Cp></Cp>
            </div>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .cp {
    background-image: url(/images/common/talisman.png);
    height: 52px;
    width: 168px;
    margin: 0 auto;
    margin-top: 5px;
    display: flex;
    .talisman {
      width: 28px;
      margin-left: 9px;
      margin-top: 11px;
    }
    .rune {
      width: 28px;
      margin-left: 5px;
      margin-top: 12px;
    }
    .rune:nth-child(2) {
      margin-left: 21px;
    }
  }

  .skill-slot-item {
    height: 28px;
    width: 28px;
    background-color: black;
    border: rgb(29, 29, 29) solid 1px;
  }
</style>
