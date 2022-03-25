<script lang="tsx">
	import { defineComponent, reactive } from "vue"
	export default defineComponent({
		name: "skill-icon",
		components: {  },
		props: {
			skill: {
				type: Object,
				required: true
			}
		},
		setup(props, { emit }) {
			function increaseSkillLv(e: MouseEvent) {
				if(props.skill.learn < props.skill.master) {
					props.skill.learn++;
				}
			}
			function reduceSkillLv(e: MouseEvent) {
				if(props.skill.learn > props.skill.default) {
					props.skill.learn--;
				}
			}

			return () => {
				return (
					<div class="skill-icon" onClick={increaseSkillLv}>
						<img src={props.skill.icon} />
						<div class="skill-lv">
							{ props.skill.learn == props.skill.master ? (
								<span class="M">M</span>) : (
								<span class="lv">Lv</span>)
							}
							<span class="num">{props.skill.learn}</span>
						</div>
					</div>
				)
			}
		}
	})
</script>
<style scoped lang="scss">
.skill-icon {
	display: inline-block;
	width: 36px; // 50
	height: 56px; // 70
	border: 1px solid #000;
	border-radius: 2px;
	background-color: #2F2F2F;
	
	&:hover {
		border-color: #64ADD0;
	}
	
	> img {
		//margin: 3px 3px 1px 3px;
		margin: 2px 2px 2px 2px;
		display: block;
		width: 30px;
		//width: 42px;
		//height: 42px;
		height: 30px;
		border: 1px solid #000;
	}
	
	.skill-lv {
		margin: 0 5px;
		background-color: #000;
		text-align: center;
		font-size: 12px;
		height: 18px;
		line-height: 18px;
		width: calc(100% - 4px);
		margin-left: 2px;
		
		.lv {
			margin-right: 3px;
			color: #FFF;
		}
		
		.M {
			margin-right: 5px;
			border: 1px solid #C6A228;
			border-radius: 3px;
			color: #C6A228;
			display: inline-block;
			height: 11px;
			line-height: 11px;
			padding: 0 1px 0 2px;
			
			+ .num {
				color: #C6A228;
			}
		}
		
		.num {
			color: #FFF;
		}
	}
}
</style>