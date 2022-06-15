<script lang="tsx">
  import { IEnchantingInfo } from "@/api/info/type"
  import { compile, computed, defineComponent, renderList } from "vue"
  import { useBasicInfoStore, useCharacterStore, useConfigStore } from "@/store"

  export default defineComponent({
    name: "clothes",
    setup(props, { emit, slots }) {
      const clothes_type = ["神器装扮", "稀有装扮", "节日装扮", "高级装扮"]

      const basicInfoStore = useBasicInfoStore()
      const characterStore = useCharacterStore()
      const configStore = useConfigStore()

      const emblem_list = computed<IEnchantingInfo[] | undefined>(() => {
        return basicInfoStore.emblem_info?.filter(item => item.rarity != "白金").sort((a, b) => (b.maxFrame ?? 0) - (a.maxFrame ?? 0))
      })

      const equipInfo = function <T>(part: string, name: string, defaultValue?: T) {
        return computed<T>({
          get() {
            return configStore.getForge(part, name) ?? defaultValue ?? 0
          },
          set(val) {
            if (val !== undefined) {
              configStore.setForge(part, name, val)
            }
          }
        })
      }

      const up_skill = computed(() => characterStore.clothes)
      const down_skill = computed(() => characterStore.clothes_bottom)
      // 武器装扮
      const wqzb_enchat = equipInfo<string | number>("武器装扮", "enchanting")
      const wqzb_left = equipInfo<string | number>("武器装扮", "socket_left")
      const wqzb_right = equipInfo<string | number>("武器装扮", "socket_right")
      // 皮肤
      const pf_enchat = equipInfo<string | number>("皮肤", "enchanting")
      const pf_left = equipInfo<string | number>("皮肤", "socket_left")
      const pf_right = equipInfo<string | number>("皮肤", "socket_right")
      // 光环
      const gh_enchat = equipInfo<string | number>("光环", "enchanting")
      const gh_left = equipInfo<string | number>("光环", "socket_left")
      const gh_right = equipInfo<string | number>("光环", "socket_right")

      return () => (
        <div class="flex flex-wrap equ-profile">
          <div class="equ-profile-item">
            <div class="row-name">武器装扮</div>
            <calc-select v-model={wqzb_enchat.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(basicInfoStore.enchanting_info?.filter(item => item.position == "武器装扮") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={wqzb_left.value} class="flex-1 !h-20px">
              <calc-option v-model={wqzb_left.value} value={0}>
                无
              </calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={wqzb_right.value} class="flex-1 !h-20px">
              <calc-option v-model={wqzb_right.value} value={0}>
                无
              </calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">皮肤</div>
            <calc-select v-model={pf_enchat.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(basicInfoStore.enchanting_info?.filter(item => item.position == "皮肤") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={pf_left.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={pf_right.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">光环</div>
            <calc-select v-model={gh_enchat.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(basicInfoStore.enchanting_info?.filter(item => item.position == "光环") ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={gh_left.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={gh_right.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">头发</div>
            <calc-select class="flex-1 !h-20px">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="flex-1 !h-20px">
              <calc-option value="0">智力</calc-option>
              <calc-option value="1">精神</calc-option>
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">头部</div>
            <calc-select class="flex-1 !h-20px">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="flex-1 !h-20px">
              <calc-option value="0">智力</calc-option>
              <calc-option value="1">精神</calc-option>
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">脸部</div>
            <calc-select class="flex-1 !h-20px">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="flex-1 !h-20px">
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">胸部</div>
            <calc-select class="flex-1 !h-20px">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="flex-1 !h-20px">
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">上衣</div>
            <calc-select class="flex-1 !h-20px">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(up_skill.value, item => (
                <calc-option value={item}>{item} Lv+1</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">腰带</div>
            <calc-select class="flex-1 !h-20px">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="flex-1 !h-20px">
              <calc-option value="0">力量</calc-option>
              <calc-option value="1">体力</calc-option>
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">下装</div>
            <calc-select class="flex-1 !h-20px">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(down_skill.value, item => (
                <calc-option value={item}>{item} Lv+1</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">鞋</div>
            <calc-select class="flex-1 !h-20px">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="flex-1 !h-20px">
              <calc-option value="0">力量</calc-option>
              <calc-option value="1">体力</calc-option>
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">套装</div>
            <calc-select class="flex-1 !h-20px">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item + "套装"}</calc-option>
              ))}
            </calc-select>
            <div class="flex-1"></div>
          </div>
        </div>
      )
    }
  })
</script>
