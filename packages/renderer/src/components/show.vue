<script lang="tsx">
  import { defineComponent, ref } from "vue"
  import SkillPanel from "@/components/internal/skill/skill-panel.vue"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"

  export default defineComponent({
    components: { SkillPanel, EquipTips },
    setup() {
      const visible = ref(false)
      const showDialog = () => (visible.value = true)
      const test = ref(-1)

      return () => (
        <div>
          <calc-tabs>
            <calc-tab value="1">套装</calc-tab>
            <calc-tab value="2">自选</calc-tab>
          </calc-tabs>
          <calc-button onClick={showDialog}>点击展开窗口</calc-button>
          <calc-button disabled>禁用</calc-button>

          <calc-checkbox>DYSB</calc-checkbox>
          <calc-select modelValue={test}>
            <calc-option value={0}>123</calc-option>

            <calc-option value={1}>467</calc-option>
          </calc-select>
          <calc-iconselect emptyLabel="点击" modelValue={test}>
            <calc-option value={0}>
              <img src="./images/characters/重霄·弹药专家·女/skill/单兵推进器.png" />
            </calc-option>

            <calc-option value={1}>
              <img src="./images/characters/重霄·弹药专家·女/skill/兵器研究.png" />
            </calc-option>
          </calc-iconselect>
          <calc-dialog modal v-model:visible={visible.value}>
            测试
          </calc-dialog>

          <skill-panel></skill-panel>
          <equip-tips
            eq={{ id: 1, icon: "/arms/swordman/katana/218.png" }}
            colums
            show-tips
          ></equip-tips>

          <div class="flex mx-12 py-12">
            <div class="flex col-6 justify-center">
              <calc-tooltip position="left">
                {{
                  default() {
                    return (
                      <img src="https://www.tianyongxian.com/dnfstatic/images/equipment/arms/swordman/katana/218.png" />
                    )
                  },
                  popper() {
                    return (
                      <div class="h-20 text-white w-20">左侧Tooltip(默认)</div>
                    )
                  }
                }}
              </calc-tooltip>
            </div>

            <div class="flex col-6 justify-center">
              <calc-tooltip>
                {{
                  default() {
                    return (
                      <img src="https://www.tianyongxian.com/dnfstatic/images/equipment/arms/swordman/katana/218.png" />
                    )
                  },
                  popper() {
                    return (
                      <div class="h-20 text-white w-20">下方ToolTip(默认)</div>
                    )
                  }
                }}
              </calc-tooltip>
            </div>

            <div class="flex col-6 justify-center">
              <calc-tooltip position="top">
                {{
                  default() {
                    return (
                      <img src="https://www.tianyongxian.com/dnfstatic/images/equipment/arms/swordman/katana/218.png" />
                    )
                  },
                  popper() {
                    return (
                      <div class="h-20 text-white w-20">上方ToolTip(默认)</div>
                    )
                  }
                }}
              </calc-tooltip>
            </div>

            <div class="flex col-6 justify-center">
              <calc-tooltip position="right">
                {{
                  default() {
                    return (
                      <img src="https://www.tianyongxian.com/dnfstatic/images/equipment/arms/swordman/katana/218.png" />
                    )
                  },
                  popper() {
                    return (
                      <div class="h-20 text-white w-20">右侧Tooltip(默认)</div>
                    )
                  }
                }}
              </calc-tooltip>
            </div>
          </div>
        </div>
      )
    }
  })
</script>
