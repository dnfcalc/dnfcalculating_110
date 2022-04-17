<script lang="tsx">
    import { computed, Ref, defineComponent, inject, renderList, PropType } from "vue"
    import { IDetailInfo } from "../type"
    export default defineComponent({
        name: "profile",
        props: {
            charName: {
                type: String,
                default: null
            },
            detailInfo: {
                type: Array as PropType<IDetailInfo[]>,
                default: null
            }
        },
        setup(props) {
            //面板显示的顺序
            const display_parts = ["护肩", "上衣", "下装", "腰带", "鞋", "武器", "称号", "手镯", "项链", "辅助装备", "戒指", "耳环", "魔法石", "宠物"]
            function partIconStyle(part: string) {
                let x = 10
                let y = 10
                let index = display_parts.findIndex(p => p == part)

                if (index == 13) index -= 7
                else if (index >= 5 && index <= 12) {
                    x += 189
                    index -= 5
                }

                x += (index % 2) * 32
                y += Math.floor(index / 2) * 32

                return {
                    left: `${x}px`,
                    top: `${y}px`
                }
            }

            function setPart(part: string) {
                return () => {
                    props.detailInfo.forEach(item => (item.position === part ? (item.active = true) : (item.active = false)))
                }
            }

            return () => (
                <div>
                    <div class="char-info">
                        <div class="head" style="background-image:url(images/common/head.png)">
                            <div
                                class="w-266px h-170px bg-bottom flex char"
                                style={"background-image:url(images/characters/" + props.charName + "/人物.png);background-repeat: no-repeat; position: absolute;"}
                            >
                                [{props.charName?.replace("·男", "").replace("·女", "")}]
                                {renderList(props.detailInfo, item => (
                                    <div onClick={setPart(item.position)} class="absolute w-7 h-7" style={partIconStyle(item.position)}>
                                        {item.position}
                                    </div>
                                ))}
                            </div>
                            <div class="h-150px w-266px" style="background-image:url(images/common/equ-back.png)"></div>
                        </div>
                    </div>
                </div>
            )
        }
    })
</script>
<style lang="scss">
    .char-info {
        width: 266px;
        height: 180px;
        position: relative;
        padding: 5px;
        font-size: 12px;

        // background-color: rgba(255, 255, 255, 0.5);
        // background-image: url("./img/60.png");
        .head {
            background-repeat: no-repeat;
            height: 177px;
            display: flex;
            justify-content: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
            .char {
                display: flex;
                justify-content: center;
                align-items: flex-end;
                color: white;
            }
        }
    }
</style>
