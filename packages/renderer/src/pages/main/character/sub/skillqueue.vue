<script lang="tsx">
  import { computed, defineComponent, reactive, ref, renderList, watch } from "vue"
  import { useCharacterStore, useConfigStore } from "@/store"
  import { skill_icon } from "./utils"
  import draggable from "@/components/vuedraggable/vuedraggable"

  export default defineComponent({
    name: "skillqueue",
    components: {
      draggable
    },
    setup(props, { emit, slots }) {
      const characterStore = useCharacterStore()
      const configStore = useConfigStore()
      let canChooseSkill = ref(configStore.skill_que)
      const colors = ["#fee86b", "#75ae1b", "#1bae83", "#1b63ae", "#b920c3", "c3207c"]

      //   watch(configStore.skill_set, val => {
      //     let tem: { name: string; id: number; mode: string; modes: string[] | undefined }[] = []
      //     // 重新排序一下
      //     //   let temp =
      //     //     configStore.skill_que?.map((item, index) => {
      //     //       item.id = index
      //     //       return item
      //     //     }) || []
      //     //   let toRemove = []
      //     //   let toAdd = []
      //     //   // 根据次数删除
      //     //   temp.map(item => item.name)
      //     // })
      //     // todo 根据次数修改自动添加/删除技能
      //     configStore.skill_set.forEach(item => {
      //       if (item.count > 0 && item.level > 0 && item.damage) for (var i = 0; i < item.count; i++) tem.push({ name: item.name, id: 0, mode: item.mode?.[0] ?? "", modes: item.mode })
      //     })
      //     configStore.skill_que = tem.map((item, index) => {
      //       item.id = index
      //       return item
      //     })
      //   })

      // watch(canChooseSkill.value, val => {
      //   configStore.skill_que = val
      // })

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
            class="h-28px m-2px w-28px"
            style={"position: relative;" + (skill.modes?.length ?? 0 > 0 ? (skill.modes?.indexOf(skill.mode) ?? 0 > 0 ? "background-color: " + colors[skill.modes?.indexOf(skill.mode) ?? 0] : 0) : "")}
            onClick={changeMode(skill)}
          >
            <img style={skill.modes?.length ?? 0 > 0 ? (skill.modes?.indexOf(skill.mode) ?? 0 > 0 ? "mix-blend-mode: luminosity;" : "") : ""} src={skill_icon(characterStore.alter, skill.name)} />
            {skill.modes && skill.modes.length > 0 && <div class="size-11">{skill.mode}</div>}
          </div>
          // <div class="list-group-item">{item.element.name}</div>
        )
      }

      return () => (
        <div class="w-300px">
          <div class="h-100% skill-slots subitem">
            <div class="head-sec">技能队列设置</div>
            <draggable class="flex flex-wrap body-sec" v-model:list={configStore.skill_que} group={{ name: "people", pull: "clone", put: false }} itemKey="id">
              {{
                item: item
              }}
            </draggable>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .size-11 {
    position: absolute;
    top: 0;
    right: -2px;
    font-size: 12px;
    transform: scale(0.85);
    color: #fee86b;
    text-shadow: #000 2px 0 0, #000 0 2px 0, #000 -2px 0 0, #000 0 -2px 0;
    -webkit-font-smoothing: antialiased;
  }
</style>
