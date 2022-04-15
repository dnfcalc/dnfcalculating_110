<script lang="tsx">
    import { defineComponent, onMounted, watch, ref, renderList, computed, reactive } from "vue"
    import { useBasicInfoStore } from "@/store"
    import { IEquipmentInfo, IWeaponInfo } from "@/api/info/type"

    import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
    import { useRoute } from "vue-router"

    interface BasicInfo {
        public_110_equ?: IEquipmentInfo[]
        char_weapon_equ?: IEquipmentInfo[]
        public_myth_euq?: IEquipmentInfo[]
    }

    interface EquiChooseState {
        id: number
        state: boolean
        hightlight?: boolean
    }

    export default defineComponent({
        components: { EquipTips },
        setup() {
            const basicStore = useBasicInfoStore()
            const route = useRoute()
            let choose_feature = ref(0)
            let basic_info = ref<BasicInfo>({})
            let equi_choose_110 = reactive<EquiChooseState[]>([])
            let equi_choose_myth = reactive<EquiChooseState[]>([])
            let equi_choose_char_weapon = reactive<EquiChooseState[]>([])

            onMounted(async () => {
                await basicStore.get_equipment_info()
                // Lv110装备
                basic_info.value.public_110_equ = basicStore?.equipmentinfo?.equipment_Lv110 as IEquipmentInfo[]
                // 110装备记录
                basic_info.value.public_110_equ.forEach(item => {
                    equi_choose_110.push({
                        id: item.id,
                        state: false,
                        hightlight: false
                    })
                })

                // 神话装备
                basic_info.value.public_myth_euq = basicStore?.equipmentinfo?.equipment_myth as IEquipmentInfo[]
                // 神话装备记录
                basic_info.value.public_myth_euq.forEach(item => {
                    equi_choose_myth.push({
                        id: item.id,
                        state: false
                    })
                })

                if (typeof route.params.name === "string") {
                    // 武器列表
                    basic_info.value.char_weapon_equ = basicStore?.equipmentinfo?.equipment_weapon.filter(
                        // item => item.name == "剑魂"
                        item => item.name == route.params.name
                    )[0].eqs as IEquipmentInfo[]

                    // 武器记录
                    basic_info.value.char_weapon_equ.forEach(item => {
                        equi_choose_char_weapon.push({
                            id: item.id,
                            state: false
                        })
                    })
                }
            })

            function changeState(equ: EquiChooseState) {
                return (e: boolean) => {
                    equ.state = e
                }
            }

            //   watch(choose_feature,searchEqu)

            function searchEqu() {
                basic_info.value?.public_110_equ?.forEach((item, index) => {
                    equi_choose_110[index].hightlight = false
                    if ((item.features?.indexOf(choose_feature.value) as number) >= 0) {
                        equi_choose_110[index].hightlight = true
                    }
                })
            }

            // 根据当前的用户选择情况及筛选情况进行全选/全部取消选择
            function selectAll(equList: EquiChooseState[], isL110: boolean = false) {
                return () => {
                    console.log("selectall :", isL110, choose_feature.value)
                    if (choose_feature.value > 0 && isL110) {
                        let totalState = equList.filter(item => item.state && item.hightlight).length > equList.length / 2
                        equList.forEach(item => {
                            item.state = item.hightlight ? !totalState : item.state
                            item.hightlight = false
                        })
                        console.log(choose_feature.value)
                        choose_feature.value = 0
                    } else {
                        let totalState = equList.filter(item => item.state).length > equList.length / 2
                        equList.forEach(item => {
                            item.state = !totalState
                        })
                    }
                }
            }

            // let equi_choose = computed<EquiChooseState[]>(() => {
            //   let list = [] as EquiChooseState[]
            //   basic_info.value?.public_110_equ?.forEach(item => {
            //     if (item.state) {
            //       list.push({ id: item.id, state: false })
            //     }
            //   })
            //   return list
            // })

            return () => (
                <div class="flex">
                    <div class="equ-105">
                        <div class="flex w-100%  mb-5px">
                            <calc-select v-model={choose_feature.value} class="ownSelect" emptyLabel="特性选择">
                                <calc-option value={0}>全部</calc-option>
                                <calc-option value={1}>出血</calc-option>
                                <calc-option value={2}>石化</calc-option>
                            </calc-select>
                            <calc-button class="w-100%" onClick={selectAll(equi_choose_110, true)}>
                                105装备
                            </calc-button>
                        </div>
                        <div>
                            {renderList(basic_info.value.public_110_equ as IEquipmentInfo[], (equ, index) => (
                                <equip-tips
                                    class="item"
                                    eq={equ}
                                    canClick={true}
                                    show-tips
                                    hightlight={equi_choose_110[index].hightlight}
                                    active={equi_choose_110[index].state}
                                    onChange={changeState(equi_choose_110[index])}
                                ></equip-tips>
                            ))}
                        </div>
                    </div>
                    <div class="equ-else">
                        <div class="equ-else-sort">
                            <calc-button class="w-100% mb-5px" onClick={selectAll(equi_choose_myth)}>
                                神话装备
                            </calc-button>
                            <div>
                                {renderList(basic_info.value.public_myth_euq as IEquipmentInfo[], (equ, index) => (
                                    <equip-tips class="item" eq={equ} canClick={true} show-tips active={equi_choose_myth[index].state} onChange={changeState(equi_choose_myth[index])}></equip-tips>
                                ))}
                            </div>
                        </div>
                        <div class="equ-else-sort">
                            <calc-button class="w-100% mb-5px">智慧产物</calc-button>
                        </div>
                        <div class="equ-else-sort">
                            <calc-button class="w-100% mb-5px" onClick={selectAll(equi_choose_char_weapon)}>
                                武器列表
                            </calc-button>

                            <div class="m-0">
                                {renderList(basic_info.value.char_weapon_equ as IEquipmentInfo[], (equ, index) => (
                                    <equip-tips
                                        class="item"
                                        eq={equ}
                                        canClick={true}
                                        show-tips
                                        active={equi_choose_char_weapon[index].state}
                                        onChange={changeState(equi_choose_char_weapon[index])}
                                    ></equip-tips>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            )
        }
    })
</script>

<style lang="scss">
    .equ-105 {
        margin: 5px;
        display: flex;
        flex-wrap: wrap;
        align-content: flex-start;
        width: 366px;
        background-color: rgba(255, 255, 255, 0.1);

        .item {
            width: 32px;
            height: 34px;

            &:nth-child(11n + 6),
            &:nth-child(11n + 9) {
                margin-left: 7px;
            }
        }
    }

    .ownSelect {
        height: calc(100% - 2px) !important;
        width: 80px !important;
        margin-right: 3px;
    }

    .equ-else {
        display: flex;
        flex-direction: column;
        width: 254px;
        margin-bottom: 5px;

        .equ-else-sort {
            margin-top: 5px;
            height: 33.3%;
            display: flex;
            flex-wrap: wrap;
            align-content: flex-start;
            background-color: rgba(255, 255, 255, 0.1);

            .item {
                width: 32px;
                height: 34px;
                margin-left: 5px;

                &:nth-child(7n + 1) {
                    margin-left: 0px;
                }
            }
        }
    }

    .imgcover::after {
        content: "";
        width: 28px;
        height: 28px;
        background-color: rgba(50, 50, 50, 0.75);
        z-index: 999;
    }
</style>
