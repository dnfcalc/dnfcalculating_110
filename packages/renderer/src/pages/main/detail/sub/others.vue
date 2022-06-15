<script lang="tsx">
  import { useConfigStore, useBasicInfoStore } from "@/store"
  import { computed, defineComponent, renderList } from "vue"

  export default defineComponent({
    name: "others",

    setup(props, { emit, slots }) {
      const configStore = useConfigStore()
      const currentInfo = function <T>(name: string, defaultValue?: T) {
        return computed<string | number>({
          get() {
            return configStore.getForge("others", name) ?? defaultValue ?? 0
          },
          set(val) {
            configStore.setForge("others", name, val)
          }
        })
      }

      const equipInfo = function <T>(part: string, name: string, defaultValue?: T) {
        return computed<string | number>({
          get() {
            return configStore.getForge(part, name) ?? defaultValue ?? 0
          },
          set(val) {
            if (val == undefined) return
            configStore.setForge(part, name, val)
          }
        })
      }
      const basicInfoStore = useBasicInfoStore()

      // 冒险团等级
      const mxtLV = currentInfo("mxtLV")
      // 工会属性
      const gh = currentInfo("gh")
      // 工会BUFF-四维
      const gh_buff_SW = currentInfo("gh_buff_SW")
      // 工会BUFF-攻击力
      const gh_buff_GJ = currentInfo("gh_buff_GJ")
      // 婚房
      const HF = currentInfo("HF")
      // 婚戒
      const HJ = currentInfo("HJ")
      // 收集箱种类
      const SJX_TYPE = currentInfo("SJX_TYPE")
      // 晶体契约
      const JTQY = currentInfo("JTQY", 0)
      // 收集箱稀有
      const SJX_XY = currentInfo("SJX_XY")
      // 收集箱神器
      const SJX_SQ = currentInfo("SJX_SQ")
      // 勋章种类
      const XZ_TYPE = currentInfo("XZ_TYPE")
      // 勋章守护珠
      const XZ_SHZ = currentInfo("XZ_SHZ")
      // 勋章强化
      const XZ_QH = currentInfo("XZ_QH")
      // 名称装扮卡
      const MCZBK = currentInfo("MCZBK")
      // 快捷装备
      const KJZB = equipInfo("快捷装备", "enchanting")

      const SJX_disabled = computed(() => {
        return SJX_TYPE.value == 0
      })

      return () => (
        <div class="flex flex-wrap equ-profile">
          <div class="equ-profile-item">
            <div class="row-name">冒险团等级</div>
            <calc-select v-model={mxtLV.value} class="!h-20px flex-1">
              {renderList(basicInfoStore.sundries_info?.filter(item => item.position == "冒险团") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">工会属性</div>
            <calc-select v-model={gh.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              {renderList(basicInfoStore.sundries_info?.filter(item => item.position == "工会属性") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div class="row-name">训练官Buff</div>
            <calc-select v-model={gh_buff_SW.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              {renderList(basicInfoStore.sundries_info?.filter(item => item.position == "工会buff-攻击力") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>

            <calc-select v-model={gh_buff_GJ.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              {renderList(basicInfoStore.sundries_info?.filter(item => item.position == "工会buff-四维强化") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div v-model={HJ.value} class="row-name">
              结婚系统
            </div>
            <calc-select v-model={HF.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              {renderList(basicInfoStore.sundries_info?.filter(item => item.position == "婚房") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>

            <calc-select v-model={HJ.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              {renderList(basicInfoStore.sundries_info?.filter(item => item.position == "婚戒") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div class="row-name">晶体契约</div>
            <calc-select v-model={JTQY.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              {renderList(basicInfoStore.sundries_info?.filter(item => item.position == "晶体契约") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div class="row-name">收集箱</div>
            <calc-select v-model={SJX_TYPE.value} emptyLabel="种类" class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              {renderList(basicInfoStore.sundries_info?.filter(item => item.position == "收集箱") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
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
              {renderList(basicInfoStore.sundries_info?.filter(item => item.position == "勋章") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={XZ_SHZ.value} class="!h-20px flex-1">
              <calc-option value={0}>无</calc-option>
              <calc-option value={5}>属强 +5</calc-option>
              <calc-option value={7}>属强 +7</calc-option>
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
            <calc-select v-model={MCZBK.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              {renderList(basicInfoStore.sundries_info?.filter(item => item.position == "名称装扮卡") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
          </div>

          <div class="equ-profile-item">
            <div class="row-name">快捷装备</div>
            <calc-select v-model={KJZB.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
              {renderList(basicInfoStore.enchanting_info?.filter(item => item.position == "快捷装备") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
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
