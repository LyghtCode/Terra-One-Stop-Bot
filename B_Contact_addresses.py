#!/usr/bin/python3

def contact_addresses(network):
    if network == 'MAINNET':
        # columbus-4
        contracts = {
            # Mirror https://docs.mirror.finance/networks#terra
            'Collector': 'terra1s4fllut0e6vw0k3fxsg4fs6fm2ad6hn0prqp3s',
            'Community': 'terra1x35fvy3sy47drd3qs288sm47fjzjnksuwpyl9k',
            'Factory': 'terra1mzj9nsxx0lxlaxnekleqdy8xnyw2qrh3uz6h8p',
            'Gov': 'terra1wh39swv7nq36pnefnupttm2nr96kz7jjddyt2x',
            'Mint': 'terra1wfz7h3aqf4cjmjcvc6s8lxdhh7k30nkczyf0mj',
            'Oracle': 'terra1t6xe0txzywdg85n6k8c960cuwgh6l8esw6lau9',
            'Staking': 'terra17f7zu97865jmknk7p2glqvxzhduk78772ezac5',
            'Airdrop': 'terra1kalp2knjm4cs3f59ukr4hdhuuncp648eqrgshw',
            'Limit Order': 'terra1zpr8tq3ts96mthcdkukmqq4y9lhw0ycevsnw89',
            'Collateral Oracle': 'terra1pmlh0j5gpzh2wsmyd3cuk39cgh2gfwk6h5wy9j',
            'Lock': 'terra169urmlm8wcltyjsrn7gedheh7dker69ujmerv2',
            'Short Reward': 'terra16mlzdwqq5qs6a23250lq0fftke8v80sapc5kye',
            # mAssets https://docs.mirror.finance/networks#terra
            'SPEC': 'terra1s5eczhe0h0jutf46re52x5z4r03c8hupacxmdr',
            'MIR': 'terra15gwkyepfc6xgca5t5zefzwy42uts8l2m4g40k6',
            'ANC': 'terra14z56l0fp2lsf86zy3hty2z47ezkhnthtr9yq76',
            'mAAPL': 'terra1vxtwu4ehgzz77mnfwrntyrmgl64qjs75mpwqaz',
            'mGOOGL': 'terra1h8arz2k547uvmpxctuwush3jzc8fun4s96qgwt',
            'mTSLA': 'terra14y5affaarufk3uscy2vr6pe6w6zqf2wpjzn5sh',
            'mNFLX': 'terra1jsxngqasf2zynj5kyh0tgq9mj3zksa5gk35j4k',
            'mQQQ': 'terra1csk6tc7pdmpr782w527hwhez6gfv632tyf72cp',
            'mTWTR': 'terra1cc3enj9qgchlrj34cnzhwuclc4vl2z3jl7tkqg',
            'mMSFT': 'terra1227ppwxxj3jxz8cfgq00jgnxqcny7ryenvkwj6',
            'mAMZN': 'terra165nd2qmrtszehcfrntlplzern7zl4ahtlhd5t2',
            'mBABA': 'terra1w7zgkcyt7y4zpct9dw8mw362ywvdlydnum2awa',
            'mIAU': 'terra15hp9pr8y4qsvqvxf3m4xeptlk7l8h60634gqec',
            'mSLV': 'terra1kscs6uhrqwy6rx5kuw5lwpuqvm3t6j2d6uf2lp',
            'mUSO': 'terra1lvmx8fsagy70tv0fhmfzdw9h6s3sy4prz38ugf',
            'mVIXY': 'terra1zp3a6q6q4953cz376906g5qfmxnlg77hx3te45',
            'mFB': 'terra1mqsjugsugfprn3cvgxsrr8akkvdxv2pzc74us7',
            'mCOIN': 'terra18wayjpyq28gd970qzgjfmsjj7dmgdk039duhph',
            # Spectrum Protocol
            # https://github.com/spectrumprotocol/frontend/blob/11de02569898be54abc716b5a651cbf064865db5/src/app/consts/networks.ts
            'mirrorFarm': 'terra1kehar0l76kzuvrrcwj5um72u3pjq2uvp62aruf',
            'anchorFarm': 'terra1fqzczuddqsdml37a20pysjx5wk9dh4tdzu2mrw',
            'specFarm': 'terra17hjvrkcwn3jk2qf69s5ldxx5rjccchu35assga',
            'pylonFarm': 'terra1r3675psl7s2fe0sfh0vut5z4hrywgyyfdrzg95',
            'specgov': 'terra1dpe4fmcz2jqk6t50plw0gqa2q3he2tj6wex5cl',
            # TerraSwap
            'Spectrum SPEC-UST Pair': 'terra1tn8ejzw8kpuc87nu42f6qeyen4c7qy35tl8t20',
            'Terraswap MIR-UST Pair': 'terra1amv303y8kzxuegvurh0gug2xe9wkgj65enq2ux',
            # Anchor
            'bLunaHub': 'terra1mtwph2juhj0rvjz7dy92gvl6xvukaxu8rfv8ts',
            'bLunaToken': 'terra1kc87mu460fwkqte29rquh4hc20m54fxwtsx7gp',
            'bLunaReward': 'terra17yap3mhph35pcwvhza38c2lkj7gzywzy05h7l0',
            'bLunaAirdrop': 'terra199t7hg7w5vymehhg834r6799pju2q3a0ya7ae9',
            'mmInterestModel': 'terra1kq8zzq5hufas9t0kjsjc62t2kucfnx8txf547n',
            'mmOracle': 'terra1cgg6yef7qcdm070qftghfulaxmllgmvk77nc7t',
            'mmMarket': 'terra1sepfj7s0aeg5967uxnfk4thzlerrsktkpelm5s',
            'mmOverseer': 'terra1tmnqgvg567ypvsvk6rwsga3srp7e3lg6u0elp8',
            'mmCustody': 'terra1ptjp2vfjrwh0j0faj9r6katm640kgjxnwwq9kn',
            'mmLiquidation': 'terra1w9ky73v4g7v98zzdqpqgf3kjmusnx4d4mvnac6',
            'mmDistributionModel': 'terra14mufqpr5mevdfn92p4jchpkxp7xr46uyknqjwq',
            'aTerra': 'terra1hzh9vpxhsk8253se0vv5jj6etdvxu3nv8z07zu',
            'terraswapblunaLunaPair': 'terra1jxazgm67et0ce260kvrpfv50acuushpjsz2y0p',
            'terraswapblunaLunaLPToken': 'terra1nuy34nwnsh53ygpc4xprlj263cztw7vc99leh2',
            'terraswapAncUstPair': 'terra1gm5p3ner9x9xpwugn9sp6gvhd0lwrtkyrecdn3',
            'terraswapAncUstLPToken': 'terra1gecs98vcuktyfkrve9czrpgtg0m3aq586x6gzm',
            'gov': 'terra1f32xyep306hhcxxxf7mlyh0ucggc00rm2s9da5',
            'distributor': 'terra1mxf7d5updqxfgvchd7lv6575ehhm8qfdttuqzz',
            'collector': 'terra14ku9pgw5ld90dexlyju02u4rn6frheexr5f96h',
            'community': 'terra12wk8dey0kffwp27l5ucfumczlsc9aned8rqueg',
            'staking': 'terra1897an2xux840p9lrh6py3ryankc6mspw49xse3',
            'ANC': 'terra14z56l0fp2lsf86zy3hty2z47ezkhnthtr9yq76',
            'airdrop': 'terra146ahqn6d3qgdvmj8cj96hh03dzmeedhsf0kxqm',
            'team_vesting': 'terra1pm54pmw3ej0vfwn3gtn6cdmaqxt0x37e9jt0za',
            'investor_vesting': 'terra10evq9zxk2m86n3n3xnpw28jpqwp628c6dzuq42'
        }
    else:
        # Bombay-12
        contracts = {
            # Mirror https://docs.mirror.finance/networks#terra
            'Collector': 'terra1v046ktavwzlyct5gh8ls767fh7hc4gxc95grxy',
            'Community': 'terra10qm80sfht0zhh3gaeej7sd4f92tswc44fn000q',
            'Factory': 'terra10l9xc9eyrpxd5tqjgy6uxrw7dd9cv897cw8wdr',
            'Gov': 'terra12r5ghc6ppewcdcs3hkewrz24ey6xl7mmpk478s',
            'Mint': 'terra1s9ehcjv0dqj2gsl72xrpp0ga5fql7fj7y3kq3w',
            'Oracle': 'terra1uvxhec74deupp47enh7z5pk55f3cvcz8nj4ww9',
            'Staking': 'terra1a06dgl27rhujjphsn4drl242ufws267qxypptx',
            'Airdrop': 'terra1p6nvyw7vz3fgpy4nyh3q3vc09e65sr97ejxn2p',
            'Limit Order': 'terra1vc4ch0z3n6c23f9uywzy5yqaj2gmpnam8qgge7',
            'Collateral Oracle': 'terra1q3ls6u2glsazdeu7dxggk8d04elnvmsg0ung6n',
            'Lock': 'terra1pcxghd4dyf950mcs0kmlp7lvnrjsnl6qlfldwj',
            # mAssets https://docs.mirror.finance/networks#terra
            'SPEC': 'terra1kvsxd94ue6f4rtchv2l6me5k07uh26s7637cza',
            'MIR': 'terra10llyp6v3j3her8u3ce66ragytu45kcmd9asj3u',
            'ANC': 'terra1747mad58h0w4y589y3sk84r5efqdev9q4r02pc',
            'mAAPL': 'terra16vfxm98rxlc8erj4g0sj5932dvylgmdufnugk0',
            'mDOT': 'terra1fs6c6y65c65kkjanjwvmnrfvnm2s58ph88t9ky',
            'mGOOGL': 'terra1qg9ugndl25567u03jrr79xur2yk9d632fke3h2',
            'mGME': 'terra104tgj4gc3pp5s240a0mzqkhd3jzkn8v0u07hlf',
            'mGS': 'terra13myzfjdmvqkama2tt3v5f7quh75rv78w8kq6u6',
            'mTSLA': 'terra1nslem9lgwx53rvgqwd8hgq7pepsry6yr3wsen4',
            'mNFLX': 'terra1djnlav60utj06kk9dl7defsv8xql5qpryzvm3h',
            'mQQQ': 'terra18yx7ff8knc98p07pdkhm3u36wufaeacv47fuha',
            'mTWTR': 'terra1ax7mhqahj6vcqnnl675nqq2g9wghzuecy923vy',
            'mMSFT': 'terra12s2h8vlztjwu440khpc0063p34vm7nhu25w4p9',
            'mAMZN': 'terra12saaecsqwxj04fn0jsv4jmdyp6gylptf5tksge',
            'mBABA': 'terra15dr4ah3kha68kam7a907pje9w6z2lpjpnrkd06',
            'mIAU': 'terra19dl29dpykvzej8rg86mjqg8h63s9cqvkknpclr',
            'mSLV': 'terra1fdkfhgk433tar72t4edh6p6y9rmjulzc83ljuw',
            'mUSO': 'terra1fucmfp8x4mpzsydjaxyv26hrkdg4vpdzdvf647',
            'mVIXY': 'terra1z0k7nx0vl85hwpv3e3hu2cyfkwq07fl7nqchvd',
            'mFB': 'terra14gq9wj0tt6vu0m4ec2tkkv4ln3qrtl58lgdl2c',
            'mCOIN': 'terra1qre9crlfnulcg0m68qqywqqstplgvrzywsg3am',
            # Spectrum Protocol
            # https://github.com/spectrumprotocol/frontend/blob/11de02569898be54abc716b5a651cbf064865db5/src/app/consts/networks.ts
            'mirrorFarm': 'terra1hasdl7l6xtegnch8mjyw2g7mfh9nt3gtdtmpfu',
            'anchorFarm': 'terra1yvpd3j7mry7qrmmn2x9vapmr9qpzkvjgs4f7z7',
            'specFarm': 'terra1cedx8gpvu7c4vzfadwmf3pewg2030fqgw4q3dl',
            'pylonFarm': 'terra1hgjp2yjqe7ngzsx283tm7ch8xcsvk5c8mdj2tw',
            'specgov': 'terra1x3l2tkkwzzr0qsnrpy3lf2cm005zxv7pun26x4',
            # TerraSwap
            'Spectrum SPEC-UST Pair': 'terra15cjce08zcmempedxwtce2y44y2ayup8gww3txr',
            'Terraswap MIR-UST Pair': 'terra1cz6qp8lfwht83fh9xm9n94kj04qc35ulga5dl0',
            # Anchor
            "bLunaHub": "terra1fflas6wv4snv8lsda9knvq2w0cyt493r8puh2e",
            "bLunaToken": "terra1u0t35drzyy0mujj8rkdyzhe264uls4ug3wdp3x",
            "bLunaReward": "terra1ac24j6pdxh53czqyrkr6ygphdeftg7u3958tl2",
            "bLunaAirdrop": "terra1334h20c9ewxguw9p9vdxzmr8994qj4qu77ux6q",
            "mmInterestModel": "terra1m25aqupscdw2kw4tnq5ql6hexgr34mr76azh5x",
            "mmOracle": "terra1p4gg3p2ue6qy2qfuxtrmgv2ec3f4jmgqtazum8",
            "mmMarket": "terra15dwd5mj8v59wpj0wvt233mf5efdff808c5tkal",
            "mmOverseer": "terra1qljxd0y3j3gk97025qvl3lgq8ygup4gsksvaxv",
            "mmCustody": "terra1ltnkx0mv7lf2rca9f8w740ashu93ujughy4s7p",
            "mmLiquidation": "terra16vc4v9hhntswzkuunqhncs9yy30mqql3gxlqfe",
            "mmDistributionModel": "terra1u64cezah94sq3ye8y0ung28x3pxc37tv8fth7h",
            "aTerra": "terra1ajt556dpzvjwl0kl5tzku3fc3p3knkg9mkv8jl",
            "terraswapblunaLunaPair": "terra13e4jmcjnwrauvl2fnjdwex0exuzd8zrh5xk29v",
            "terraswapblunaLunaLPToken": "terra1tj4pavqjqjfm0wh73sh7yy9m4uq3m2cpmgva6n",
            "terraswapAncUstPair": "terra1wfvczps2865j0awnurk9m04u7wdmd6qv3fdnvz",
            "terraswapAncUstLPToken": "terra1vg0qyq92ky9z9dp0j9fv5rmr2s80sg605dah6f",
            "gov": "terra16ckeuu7c6ggu52a8se005mg5c0kd2kmuun63cu",
            "distributor": "terra1z7nxemcnm8kp7fs33cs7ge4wfuld307v80gypj",
            "collector": "terra1hlctcrrhcl2azxzcsns467le876cfuzam6jty4",
            "community": "terra17g577z0pqt6tejhceh06y3lyeudfs3v90mzduy",
            "staking": "terra19nxz35c8f7t3ghdxrxherym20tux8eccar0c3k",
            "ANC": "terra1747mad58h0w4y589y3sk84r5efqdev9q4r02pc",
            "airdrop": "terra1u5ywhlve3wugzqslqvm8ks2j0nsvrqjx0mgxpk",
            "investor_vesting": "not available in testnet",
            "team_vesting": "not available in testnet"
        }
    return contracts

# Create a reverse dictionary to look up names for contracts
def rev_contact_addresses(contact_addresses):
    rev_contact_addresses = dict((v, k) for k, v in contact_addresses.items())
    return rev_contact_addresses
