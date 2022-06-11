<script lang="tsx">
  import { defineComponent, ref, renderList, computed, reactive, watch, onMounted } from "vue"
  import Profile from "@/components/internal/profile.vue"
  import { useBasicInfoStore, useConfigStore, useDetailsStore } from "@/store"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import { IEquipmentInfo } from "@/api/info/type"
  import { useOpenWindow } from "@/hooks/open"
  import { useAsyncState } from "@vueuse/core"
  import openURL from "@/utils/openURL"

  const EPIC_EQUIP = 0

  const MYTHIC_EQUIP = 1

  const WIDSDOM_EQUIP = 2

  const WEAPON = 3

  const TITLEANFPET = 4

  export default defineComponent({
    async setup() {
      const type = ref(EPIC_EQUIP)
      const configStore = useConfigStore()
      const basicStore = useBasicInfoStore()
      const detailsStore = useDetailsStore()

      const equips = computed(() => basicStore.equipment_info?.lv110 ?? [])
      const weapons = computed(() => basicStore.equipment_info?.weapon ?? [])
      const myths = computed(() => basicStore.equipment_info?.myth ?? [])
      const wisdom = computed(() => basicStore.equipment_info?.wisdom ?? [])
      const title_pet = computed(() => [...(basicStore.equipment_info?.pet ?? []), ...(basicStore.equipment_info?.title ?? [])])

      const result = useAsyncState(() => configStore.calc(true), { id: undefined, equips: [], name: "", alter: "", skills: [], sumdamage: 0 }, {})

      function isActive(equ: IEquipmentInfo) {
        return configStore.single_set.findIndex(e => e === equ.id) > -1
      }

      const curEquList = computed(() => {
        return basicStore.equipment_list.filter(item => configStore.single_set.includes(item.id)).sort((a, b) => a.id - b.id)
      })

      function getEquip(index: number) {
        switch (type.value) {
          case WEAPON:
            return weapons.value[index]
          case MYTHIC_EQUIP:
            return myths.value[index]
          case WIDSDOM_EQUIP:
            return wisdom.value[index]
          case TITLEANFPET:
            return title_pet.value[index]

          case EPIC_EQUIP: {
            const per = 13
            const mod = index % per
            if ([5, 9].includes(mod)) {
              return undefined
            }

            index -= Math.trunc(index / per) * 2

            if (mod > 5) {
              index--
            }

            if (mod > 9) {
              index--
            }
            return equips.value[index]
          }
        }
      }

      function chooseEqu(equ: IEquipmentInfo) {
        return () => {
          configStore.single_set = configStore.single_set.sort((a, b) => a - b)
          const index = curEquList.value.findIndex(item => item.typeName == equ.typeName)
          if (index < 0) {
            configStore.single_set.push(equ.id)
          } else {
            configStore.single_set[index] = equ.id
          }
        }
      }

      function selectSuit(index: number) {
        return (e: Event) => {
          e.stopPropagation()
          if (type.value == EPIC_EQUIP) {
            const per = 13
            const mod = index % per

            const line = Math.trunc(index / per)

            let end = index

            if (mod > 9) {
              index = line * per + 8
              end = index + 3
            } else if (mod > 5) {
              index = line * per + 5
              end = index + 3
            } else {
              index = line * per
              end = index + 5
            }

            index -= line * 2
            end -= line * 2

            const equip = equips.value.slice(index, end)

            equip.map(chooseEqu).forEach(v => v?.())
          }
        }
      }

      watch(curEquList, async val => {
        if (val.map(item => item.typeName).length < 12) {
          return
        }
        await result.execute()
      })

      const openDetail = () => openURL(`/result?res=${result.state.value.id}` + (detailsStore.standard_uuid ? `&standard=${detailsStore.standard_uuid}` : ""), { width: 890, height: 600 })

      function setStandard() {
        if (result.state.value.sumdamage > 0) {
          detailsStore.setStandard(result.state.value.id)
        }
      }

      // onMounted(async () => {
      //   if (curEquList.value.map(item => item.typeName).length < 12) return
      //   result.value = await configStore.calc(true)
      // })

      // const showequ = () => {}

      return () => (
        <div class="flex singleset">
          <div class="flex flex-col m-7px mb-0">
            <div class="h-25px">
              <calc-tabs item-class="h-6 !w-20%" v-model={type.value}>
                <calc-tab value={EPIC_EQUIP}>史诗</calc-tab>
                <calc-tab value={MYTHIC_EQUIP}>神话</calc-tab>
                <calc-tab value={WIDSDOM_EQUIP}>智慧产物</calc-tab>
                <calc-tab value={WEAPON}>武器</calc-tab>
                <calc-tab value={TITLEANFPET}>称号 宠物</calc-tab>
              </calc-tabs>
            </div>
            <div class="h-140 w-120 overflow-y-auto equ">
              {renderList(325, (item, index) => {
                const equ = getEquip(index)
                return (
                  <div class="equ-item">
                    {equ && <EquipTips onClick={chooseEqu(equ)} onDblclick={selectSuit(index)} active={isActive(equ)} eq={equ} key={equ.id} canClick={true} show-tips={false}></EquipTips>}
                  </div>
                )
              })}
            </div>
          </div>
          <div>
            <div class="flex h-24px mt-7px items-center justify-between !mr-8px !ml-8px">
              <calc-button class="!w-30%" onClick={setStandard}>
                设为基准
              </calc-button>
              <calc-button class="!w-30%" onClick={() => detailsStore.setStandard(undefined)}>
                清空基准
              </calc-button>
              <calc-button class="!w-30%" onClick={() => openDetail()}>
                查看详情
              </calc-button>
            </div>
            <Profile
              standardSum={detailsStore.standard?.sumdamage}
              details={result.state.value.info}
              sumdamage={result.state.value.sumdamage}
              equ-list={curEquList.value}
              class="m-5px !mt-0 !mr-2px !ml-2px"
            ></Profile>
          </div>
          <div class="flex m-10px mr-2px mb-0 ml-2px w-350px justify-center">辟邪玉提升率(理论值仅供参考)</div>
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
