<script lang="tsx">
  import { useCharacterStore } from "@/store"
  import { computed, defineComponent, renderList } from "vue"

  export default defineComponent({
    name: "others",

    setup(props, { emit, slots }) {
      const characterStore = useCharacterStore()
      const currentInfo = function <T>(name: string, defaultValue?: T) {
        return computed<string | number>({
          get() {
            return characterStore.getForge("jade", name) ?? defaultValue ?? 0
          },
          set(val) {
            characterStore.setForge("jade", name, val)
          }
        })
      }

      // 冒险团等级
      const mxtLV = currentInfo("mxtLV", 28)
      // 工会属性
      const gh = currentInfo("gh", 2)
      // 工会BUFF-四维
      const gh_buff_SW = currentInfo("gh_buff_SW")
      // 工会BUFF-攻击力
      const gh_buff_GJ = currentInfo("gh_buff_GJ")
      // 婚房
      const HF = currentInfo("HF", 2)
      // 婚戒
      const HJ = currentInfo("HJ", 4)
      // 收集箱种类
      const SJX_TYPE = currentInfo("SJX_TYPE")
      // 晶体契约
      const JTQY = currentInfo("JTQY", 1)
      // 收集箱稀有
      const SJX_XY = currentInfo("SJX_XY")
      // 收集箱神器
      const SJX_SQ = currentInfo("SJX_SQ")
      // 勋章种类
      const XZ_TYPE = currentInfo("XZ_TYPE", 1)
      // 勋章守护珠
      const XZ_SHZ = currentInfo("XZ_SHZ", 2)
      // 勋章强化
      const XZ_QH = currentInfo("XZ_QH")
      // 名称装扮卡
      const MCZBK = currentInfo("MCZBK")
      // 快捷装备
      const KJZB = currentInfo("KJZB")

      const SJX_disabled = computed(() => {
        return SJX_TYPE.value == 0
      })

      return () => (
        <div class="flex flex-wrap equ-profile">
          <div class="equ-profile-item">
            <div class="row-name">冒险团等级</div>
            <calc-select v-model={mxtLV.value} class="!h-20px flex-1">
              {renderList(50, i => (
                <calc-option value={i}>{i}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">工会属性</div>
            <calc-select v-model={gh.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              <calc-option value="1">四维 + 60</calc-option>
              <calc-option value="2">四维 + 120</calc-option>
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div class="row-name">训练官Buff</div>
            <calc-select v-model={gh_buff_SW.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              <calc-option value="1">攻击力Lv1: 25</calc-option>
              <calc-option value="2">攻击力Lv2: 30</calc-option>
              <calc-option value="3">攻击力Lv3: 35</calc-option>
              <calc-option value="4">攻击力Lv4: 50</calc-option>
            </calc-select>

            <calc-select v-model={gh_buff_GJ.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              <calc-option value="1">四维强化Lv1: 40</calc-option>
              <calc-option value="2">四维强化Lv2: 50</calc-option>
              <calc-option value="3">四维强化Lv3: 60</calc-option>
              <calc-option value="4">四维强化Lv4: 80</calc-option>
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div v-model={HJ.value} class="row-name">
              结婚系统
            </div>
            <calc-select v-model={HF.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              <calc-option value="1">体精 +8</calc-option>
              <calc-option value="2">体精 +10 力智 +15</calc-option>
            </calc-select>

            <calc-select v-model={HJ.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              <calc-option value="1">全属强 +1</calc-option>
              <calc-option value="2">全属强 +3</calc-option>
              <calc-option value="3">全属强 +5 三攻 +5</calc-option>
              <calc-option value="4">全属强 +8 物魔攻 +10 独立+20</calc-option>
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div class="row-name">晶体契约</div>
            <calc-select v-model={JTQY.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              <calc-option value="1">无色契约:三攻 +40</calc-option>
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div class="row-name">收集箱</div>
            <calc-select v-model={SJX_TYPE.value} emptyLabel="种类" class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              <calc-option value="1">春节套</calc-option>
              <calc-option value="2">夏日套</calc-option>
            </calc-select>
            <calc-select v-model={SJX_XY.value} disabled={SJX_disabled.value} class="!h-20px flex-1">
              {renderList(6, i => (
                <calc-option value={i - 1}>稀有: {i - 1}个</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={SJX_SQ.value} disabled={SJX_disabled.value} class="!h-20px flex-1">
              {renderList(6, i => (
                <calc-option value={i - 1}>神器: {i - 1}个</calc-option>
              ))}
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div class="row-name">勋章</div>
            <calc-select v-model={XZ_TYPE.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              <calc-option value="1">力智+48 攻击力+30</calc-option>
            </calc-select>
            <calc-select v-model={XZ_SHZ.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              <calc-option value="1">属强 +5</calc-option>
              <calc-option value="2">属强 +7</calc-option>
            </calc-select>
            <calc-select v-model={XZ_QH.value} class="!h-20px flex-1">
              {renderList(21, i => (
                <calc-option value={i - 1}>强化: {i - 1}</calc-option>
              ))}
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div v-model={MCZBK.value} class="row-name">
              名称装扮卡
            </div>
            <calc-select class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              <calc-option value="1">四维 +3 三速 +1%</calc-option>
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div class="row-name">快捷装备</div>
            <calc-select v-model={KJZB.value} class="!h-20px flex-1"></calc-select>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss" scoped>
  .row-name {
    flex: 0 0 80px !important;
    text-align: center;
  }
</style>
