<script lang="tsx">
  import { defineComponent, ref, renderList, computed, reactive, watch } from "vue"
  import profile from "@/components/internal/profile.vue"
  import { useBasicInfoStore, useCharacterStore } from "@/store"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import { IEquipmentInfo } from "@/api/info/type"

  export default defineComponent({
    components: { profile, EquipTips },
    setup() {
      const type = ref("防具")
      const charStore = useCharacterStore()
      const basicStore = useBasicInfoStore()
      const chooseEquList = computed<IEquipmentInfo[]>({
        get() {
          return charStore.single_set
        },
        set(val) {
          charStore.single_set = val
        }
      })

      const equips = computed(() => basicStore.equipment_info?.lv110 ?? [])
      const weapons = computed(() => basicStore.equipment_info?.weapon ?? [])
      const myths = computed(() => basicStore.equipment_info?.myth ?? [])
      const wisdom = computed(() => basicStore.equipment_info?.wisdom ?? [])

      const currentList = computed(() => {
        if (type.value == "武器") return weapons.value
        if (type.value == "神话") return myths.value
        if (type.value == "智慧产物") return wisdom.value
        let typeNames: string[] = []
        if (type.value == "防具") typeNames = ["上衣", "下装", "头肩", "腰带", "鞋"]
        if (type.value == "首饰") typeNames = ["手镯", "项链", "戒指"]
        if (type.value == "特殊装备") typeNames = ["辅助装备", "魔法石", "耳环"]
        return equips.value.filter(item => typeNames.indexOf(item.typeName) >= 0)
      })

      const showequ = computed(() => {
        return (index: number) => {
          if (["武器", "神话", "智慧产物"].indexOf(type.value) >= 0) return currentList.value[index] ?? undefined
          let per = 4
          if (type.value == "防具") per = 6
          if ((index + 1) % per == 0) return undefined
          let showIndex = Math.trunc(index / per) * (per - 1) + (index % per)
          return currentList.value[showIndex] ?? undefined
        }
      })

      const chooseEqu = (equ: IEquipmentInfo | undefined) => {
        return () => {
          if (!equ) return
          const index = chooseEquList.value.findIndex(item => item.typeName == equ.typeName)
          if (index < 0) {
            chooseEquList.value.push(equ)
          } else {
            chooseEquList.value[index] = equ
          }
        }
      }

      // const showequ = () => {}

      return () => (
        <div class="flex singleset">
          <div class="w-445px m-7px flex flex-col">
            <div class="h-25px">
              <calc-tabs v-model:modelValue={type.value}>
                <calc-tab value="防具" class="!w-60px !h-22px !leading-22px">
                  防具
                </calc-tab>
                <calc-tab value="首饰" class="!w-60px !h-22px !leading-22px">
                  首饰
                </calc-tab>
                <calc-tab value="特殊装备" class="!w-60px !h-22px !leading-22px">
                  特殊装备
                </calc-tab>

                <calc-tab value="神话" class="!w-60px !h-22px !leading-22px">
                  神话
                </calc-tab>
                <calc-tab value="智慧产物" class="!w-60px !h-22px !leading-22px">
                  智慧产物
                </calc-tab>
                <calc-tab value="武器" class="!w-60px !h-22px !leading-22px">
                  武器
                </calc-tab>
              </calc-tabs>
            </div>
            <div class="h-625px equ">
              {renderList(180, index => (
                <div onClick={chooseEqu(showequ.value(index - 1))} class="equ-item">
                  {showequ.value(index - 1) && <EquipTips eq={showequ.value(index - 1)} canClick={true} show-tips={false}></EquipTips>}
                </div>
              ))}
            </div>
          </div>
          <div class="w-350px m-10px ml-2px mr-2px bg-gray-500">辟邪玉</div>
          <div>
            <profile equList={chooseEquList.value} class="!m-5px !ml-2px !mr-2px"></profile>
          </div>
        </div>
      )
    }
  })
</script>
<style lang="scss" scoped>
  .singleset {
    .equ {
      display: flex;
      flex-wrap: wrap;
      padding: 5px;
      background-color: rgba(0, 0, 0, 0.45);
      .equ-item {
        width: 30px;
        height: 30px;
        background-color: rgba(0, 0, 0, 0.5);
        border: 1px solid #1a1a1a;
        margin-right: 4px;
        margin-bottom: 4px;

        // &:hover {
        //   width: 30px;
        //   height: 30px;
        //   z-index: 3;
        //   background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDcuMS1jMDAwIDc5LmRhYmFjYmIsIDIwMjEvMDQvMTQtMDA6Mzk6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMy4wIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpGMjlBNkIyMUE0NTgxMUVDOTMwM0UwOTYyOTA5Q0M2RCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpGMjlBNkIyMkE0NTgxMUVDOTMwM0UwOTYyOTA5Q0M2RCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkYyOUE2QjFGQTQ1ODExRUM5MzAzRTA5NjI5MDlDQzZEIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkYyOUE2QjIwQTQ1ODExRUM5MzAzRTA5NjI5MDlDQzZEIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+7pxKFgAABXFJREFUeNrEV0uS40QQzdTf3e6mpyfgCLBmzXU4FZdiSXCBIWCAjplu27KkquTlq5JcNrMfK0rfrHz5z7SamXyNX+Mn/eVtkO+rgywSZbIgo+RlUU64niHdWUwmrBn3AZtWeWtfqtKJSu8L93e4DlrJgK++etx3uDZSyW/xW/t5/y+BCRp4zIA+Y9sEsnUFkC+4Rlyx1MTNZBm6AnWNVeWj5lPDO5UWFB0oe+zswKmRH6qPLmoCnvA6OqiNeHrFpjdsw9JRWjtL0FmCLdgWxPVVvQDXhKgAUUurWKDqANTi3Li+ugfVPXbtgTG4gTdTw5SLn7E+g8VfePs3ri+4fgazozQAbwA+QrgJtIGCGljoBtqrw7QwcS873PUweKMPoHgHvu8psu8w0G/A7k8FcAVtO/kIsA/48ie+fAKLV6wRX2c5QYBJF1jIoYUsHNh122kLQOgK4MFBoaHJEyhP4mrNNmBPMvkFGAFV6QR5D3jzQtBB/gCTf2j6CZvP4qABGs+4C9S4ojc1A3fYD3Dd+RnfHyDqEcK6K3cAf4fnR0bSBnwCWW2uB8yqn8DyhaAP0L7Xg5ieADhy0+T+pr4psJQh1KQDWru+ERpPsM4bed/JYk+w2RFaT8ycK+BG3HcTrkfIBzD4t9NXyHiANZxiYQBajn/mYT5SeCGS1ZMKYiEOXhGAYj12vAL0AKtO4rBLqfHZIl949HognV06kBui2kF32CL4JtzkK95kcizeRRmZcjV4HsH7SEeN4OEuCqlirelkzNMIX3v0nkh0hokmappAlwxqGWT9rYCWU8Xo/QDPny0BnszXwioR5ApYCOwmbEAwAmQE2EzTLoVGq8ay5mN+X+X7mcDRfUnTuu0QlJ6GuTxdAS9rJVL3YqAvPF+jeuzGrG1p3lVrLTS3zC+S/URNkQFYo82Zr1u1AI55ozJJEvOFYZSYXJtXi/u4mTf9Ap+NRTYpMNOOlrS1lftmokuESvbS9c9u7rWwgP7PEpaPhfayXOfSEUvgKm+vmBpJgCaXQ+XX6sasazRXxbMW6/qnxVEVbTGVPtUN2Gtvh9pb5xaQQL6k/artKkC1wfjuNme4Zr6OEa0AblXXEoAi74XeC36qRkqacANaplCpdareSpG9cYCXNcgQlCdLAgQtulOXzUpC7zAofGxtKPhewxPAnJkvNwF2a+aG/aqVxMt5dgCfcteuy7bY0wwA9okBZc+BBx0A3oF0V5jUbqI5btGR3NEkYG05b7Tm4B27VoDWk/koUQDvNE0OPfsKmpruSF5j6VU51Kz5cqNltYEKPduzWbjwVALcZnOBKjbgC3D2Sg9tdwS9w/Y7fvGSec6aubRGqatLYmzx6owbTl7RenaorAbPM6eu+ksau1d6gvrkIGiKXurQKXIldz+1kBw1HNeFWq+JlXY3dE4L2nuY9QH7HvHlHhlyR3M3/FZMIMO6lU3cQZ/YnY4APToY+9PIou/Hic0jVTZmg9ZMnx009QmkobV8EHgmrxr3yXUtd1yAtcqTkw+mTzAVmKv36QFl7oFNfMRxYrcBNLrYkls6vQv/9VrTXg4+QIEG2gpHn+/Is9V70N0A93zwpHJJnxk+7qdFvoGmBwCOBDxR44XD4ZL7jBZzF4NTE3gPE7f6iC/PHPbc5OLpWZq6ZbD4/Ltn1AUGwxP8dMqAPnXN7KmX9hYLH1egVbz3OabBNU2bg7ln93DFHjS+UoBtwDWBm22gCQz/ewaXa+eTw5mAgR267DQuf9SUUlUx1lcwf60tbZEqRC8pEgqNf6xr+TUEpoTx/0JLrdOUlaatwL8uaXlPjUUjdAm8FNJa0HzhffoPEnOtV2bGLL/H9/ITtPtaf9r+E2AA4bfLT+prOiQAAAAASUVORK5CYII=);
        //   background-size: 100% 100%;
        // }
      }
    }
  }
</style>
