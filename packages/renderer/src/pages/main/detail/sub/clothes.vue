<script lang="tsx">
  import { IEnchantingInfo } from "@/api/info/type"
  import { compile, computed, defineComponent, renderList } from "vue"
  import { useBasicInfoStore, useCharacterStore, useDetailsStore } from "@/store"

  export default defineComponent({
    name: "clothes",
    setup(props, { emit, slots }) {
      const clothes_type = ["神器装扮", "稀有装扮", "节日装扮", "高级装扮"]

      const basicInfoStore = useBasicInfoStore()
      const characterStore = useCharacterStore()

      const emblem_list = computed<IEnchantingInfo[] | undefined>(() => {
        return basicInfoStore.emblem_info?.filter(item => item.rarity != "白金")
      })

      const up_skill = computed(() => characterStore.clothes)
      const down_skill = computed(() => characterStore.clothes_bottom)

      return () => (
        <div class="flex flex-wrap equ-profile">
          <div class="equ-profile-item">
            <div class="row-name">武器装扮</div>
            <calc-select class="!h-20px flex-1">
              <calc-option value={0}>无</calc-option>
              {renderList([40, 45, 60, 70, 75, 80], item => (
                <calc-option value={item}>{item + "技能 Lv+1"}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">皮肤</div>
            <calc-select class="!h-20px flex-1">
              <calc-option></calc-option>
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">光环</div>
            <calc-select class="!h-20px flex-1"></calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">头发</div>
            <calc-select class="!h-20px flex-1">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value="0">智力</calc-option>
              <calc-option value="1">精神</calc-option>
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">头部</div>
            <calc-select class="!h-20px flex-1">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value="0">智力</calc-option>
              <calc-option value="1">精神</calc-option>
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">脸部</div>
            <calc-select class="!h-20px flex-1">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">胸部</div>
            <calc-select class="!h-20px flex-1">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">上衣</div>
            <calc-select class="!h-20px flex-1">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value={0}>无</calc-option>
              {renderList(up_skill.value, item => (
                <calc-option value={item}>{item} Lv+1</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">腰带</div>
            <calc-select class="!h-20px flex-1">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value="0">力量</calc-option>
              <calc-option value="1">体力</calc-option>
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">下装</div>
            <calc-select class="!h-20px flex-1">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item} Lv+1</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value={0}>无</calc-option>
              {renderList(down_skill.value, item => (
                <calc-option value={item}>{item}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">鞋</div>
            <calc-select class="!h-20px flex-1">
              {renderList(clothes_type, (item, index) => (
                <calc-option value={index}>{item}</calc-option>
              ))}
            </calc-select>
            <calc-select class="!h-20px flex-1">
              <calc-option value="0">力量</calc-option>
              <calc-option value="1">体力</calc-option>
              <calc-option value="-1">其它</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">套装</div>
            <calc-select class="!h-20px flex-1">
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
