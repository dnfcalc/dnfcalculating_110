<script lang="tsx">
  import { TreeNode } from "@/components/calc/tree/types"
  import { useDialog } from "@/components/hooks/dialog"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import SkillPanel from "@/components/internal/skill/skill-panel.vue"
  import { defineComponent, ref, VNode } from "vue"

  export default defineComponent({
    components: { SkillPanel, EquipTips },
    setup() {
      const visible = ref(false)
      const { alert } = useDialog()
      const showDialog = async () => {
        const result = await alert({ content: "测试" })
        if (result.isOk) {
          console.log("点击了确定")
        } else {
          console.log("点击了取消")
        }
      }
      const test = ref(-1)
      const node: TreeNode[] = [
        {
          label: "测试0",
          value: 0,
          children: [
            { label: "测试1", value: 1 },
            { label: "测试2", value: 2 },
            { label: "测试3", value: 3 },
            { label: "测试4", value: 4 },
            { label: "测试5", value: 5 }
          ]
        },
        {
          label: "测试6",
          value: 6,
          children: [
            { label: "测试7", value: 7 },
            { label: "测试8", value: 8 },
            { label: "测试9", value: 9 },
            { label: "测试10", value: 10 },
            { label: "测试11", value: 11 }
          ]
        }
      ]

      const model = ref(["1", "2"])

      function wrapper(title: string, element: JSX.Element | string | VNode) {
        return (
          <div class="py-2 px-4">
            <div class="font-bold h-8 text-lg text-hex-c6b083 leading-8">{title}</div>
            {element}
          </div>
        )
      }

      return () => (
        <div>
          {wrapper(
            "Tab 页签",
            <calc-tabs>
              <calc-tab value="1">套装</calc-tab>
              <calc-tab value="2">自选</calc-tab>
            </calc-tabs>
          )}

          {wrapper(
            "Button 按钮",
            <div class="flex  space-x-4 items-center">
              <calc-button onClick={showDialog}>点击展开窗口</calc-button>
              <calc-button disabled>禁用</calc-button>
            </div>
          )}

          <calc-checkbox v-model={visible.value}>DYSB</calc-checkbox>
          <div class="flex w-20">
            <calc-select modelValue={test.value}>
              <calc-option value={0}>123</calc-option>

              <calc-option value={1}>467</calc-option>
            </calc-select>
          </div>

          <calc-cascader items={node} depth="1" />

          <calc-select editable multiple v-model={test.value}>
            <calc-option value={0}>123</calc-option>
            <calc-option value={1}>467</calc-option>
          </calc-select>
          <div>{test}</div>
          <calc-iconselect emptyLabel="点击" modelValue={test.value}>
            <calc-option value={0}>
              <img src="./images/characters/重霄·弹药专家·女/skill/单兵推进器.png" />
            </calc-option>

            <calc-option value={1}>
              <img src="./images/characters/重霄·弹药专家·女/skill/兵器研究.png" />
            </calc-option>
          </calc-iconselect>
          <calc-selection onChange={(val: any) => console.log(val)} v-model={model.value} item-class="border-1  " unactive-class="text-red bg-white" active-class="bg-hex-f00 text-white" multiple>
            <calc-option>123</calc-option>

            <calc-option>467</calc-option>
          </calc-selection>

          <div class="flex mx-12 py-12">
            <div class="flex col-6 justify-center">
              <calc-tooltip position="left">
                {{
                  default() {
                    return <img src="https://www.tianyongxian.com/dnfstatic/images/equipment/arms/swordman/katana/218.png" />
                  },
                  popper() {
                    return <div class="h-20 text-white w-20">左侧Tooltip(默认)</div>
                  }
                }}
              </calc-tooltip>
            </div>

            <div class="flex col-6 justify-center">
              <calc-tooltip>
                {{
                  default() {
                    return <img src="https://www.tianyongxian.com/dnfstatic/images/equipment/arms/swordman/katana/218.png" />
                  },
                  popper() {
                    return <div class="h-20 text-white w-20">下方ToolTip(默认)</div>
                  }
                }}
              </calc-tooltip>
            </div>

            <div class="flex col-6 justify-center">
              <calc-tooltip position="top">
                {{
                  default() {
                    return <img src="https://www.tianyongxian.com/dnfstatic/images/equipment/arms/swordman/katana/218.png" />
                  },
                  popper() {
                    return <div class="h-20 text-white w-20">上方ToolTip(默认)</div>
                  }
                }}
              </calc-tooltip>
            </div>

            <div class="flex col-6 justify-center">
              <calc-tooltip position="right">
                {{
                  default() {
                    return <img src="https://www.tianyongxian.com/dnfstatic/images/equipment/arms/swordman/katana/218.png" />
                  },
                  popper() {
                    return <div class="h-20 text-white w-20">右侧Tooltip(默认)</div>
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
