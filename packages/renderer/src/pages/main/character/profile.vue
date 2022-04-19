<script lang="tsx">
  import { useCharacterStore } from "@/store"
  import { defineComponent } from "vue"

  interface IDetail {
    mingwang: number
    zhanjie: {
      zhili?: number
      liliang?: number
      wuligongji?: number
      mofagongji?: number
      duligongji?: number
      huo?: number
      bing?: number
      guang?: number
      an?: number
    }
    jintu: {
      zhili?: number
      liliang?: number
      wuligongji?: number
      mofagongji?: number
      duligongji?: number
      huo?: number
      bing?: number
      guang?: number
      an?: number
    }
  }

  enum ICONS {
    "力量",
    "智力",
    "物理攻击",
    "魔法攻击",
    "物理暴击",
    "魔法暴击",
    "攻击速度",
    "施放速度",
    "移动速度",
    "命中率",
    "独立攻击",
    "攻击属性",
    "体力",
    "精神"
  }

  export default defineComponent({
    name: "char-info",
    props: {
      eq: {
        type: Object,
        default: () => {}
      },
      charName: {
        type: String,
        default: null
      },
      charType: {
        type: String,
        default: "魔法固伤"
      },
      details: {
        type: Object,
        default: () => {}
      }
    },
    setup(props, { emit }) {
      let details = props.details as IDetail
      details.zhanjie = {
        huo: 999,
        bing: 999,
        guang: 999,
        an: 999
      }

      const character = useCharacterStore()

      return () => {
        return (
          <div class="char-info">
            <div class="head" style="background-image:url(images/common/head.png)">
              <div class="w-266px h-170px bg-bottom flex char" style={"background-image:url(images/characters/" + character.alter + "/人物.png);background-repeat: no-repeat; position: absolute;"}>
                [{character.name}]
              </div>
              <div class="h-150px w-266px" style="background-image:url(images/common/equ-back.png)"></div>
            </div>
            <div class="mingwang">
              <img src="./images/common/mingwang.png" />
              <div class="text-hex-836832 ml-2px">冒险家名望</div>
              <div class="text-hex-3ea74e ml-8px" style="width:55px">
                {details?.mingwang}
              </div>
            </div>
            <div class="details">
              <div class="de-item">
                <img class="w-15px h-15px" src={"./images/common/icon/" + ICONS.力量 + ".png"} />
                <div class="text-hex-836832 name">力量</div>
                <div class="text-hex-3ea74e">{details?.zhanjie.liliang}</div>
              </div>
              <div class="de-item">
                <img class="w-15px h-15px" src={"./images/common/icon/" + ICONS.智力 + ".png"} />
                <div class="text-hex-836832 name">智力</div>
                <div class="text-hex-3ea74e">{details?.zhanjie.zhili}</div>
              </div>

              <div class="de-item">
                <img class="w-15px h-15px" src={"./images/common/icon/" + ICONS.物理攻击 + ".png"} />
                <div class="text-hex-836832 name">物理攻击</div>
                <div class="text-hex-3ea74e">{details?.zhanjie.wuligongji}</div>
              </div>

              <div class="de-item">
                <img class="w-15px h-15px" src={"./images/common/icon/" + ICONS.魔法攻击 + ".png"} />
                <div class="text-hex-836832 name">魔法攻击</div>
                <div class="text-hex-3ea74e">{details?.zhanjie.mofagongji}</div>
              </div>

              <div class="de-item">
                <img class="w-15px h-15px" src={"./images/common/icon/" + ICONS.独立攻击 + ".png"} />
                <div class="text-hex-836832 name">独立攻击</div>
                <div class="text-hex-3ea74e">{details?.zhanjie.duligongji}</div>
              </div>

              <div class="de-item">
                <img class="w-15px h-15px" src={"./images/common/icon/" + ICONS.攻击属性 + ".png"} />
                <div class="text-hex-836832 name">攻击属性</div>
                <div class="text-hex-3ea74e">{`火(${details?.zhanjie.huo})/冰(${details?.zhanjie.bing})/光(${details?.zhanjie.guang})/暗(${details?.zhanjie.an})`}</div>
              </div>
            </div>
          </div>
        )
      }
    }
  })
</script>
<style lang="scss">
  .char-info {
    width: 266px;
    height: 368px;
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

    .mingwang {
      height: 25px;
      background-color: rgba(0, 0, 0, 0.7);
      margin-top: 1px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .details {
      height: 160px;
      -webkit-font-smoothing: none;
      background-color: rgba(0, 0, 0, 0.7);
      margin-top: 1px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      .de-item {
        height: 20px;
        display: flex;
        align-items: center;
        img {
          padding-left: 5px;
          padding-right: 5px;
          width: 15px;
          height: 15px;
        }

        .name {
          width: 50px;
        }
      }
    }
  }
</style>
