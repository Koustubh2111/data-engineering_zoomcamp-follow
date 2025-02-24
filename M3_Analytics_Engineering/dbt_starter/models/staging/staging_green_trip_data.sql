with source as (
    select * from {{ source('staging', 'rides_21_3') }}
),

renamed as (
    select
        {{ dbt_utils.generate_surrogate_key(['vendorid', 'lpep_pickup_datetime']) }} as tripid,
        vendorid,
        lpep_pickup_datetime,
        lpep_dropoff_datetime,
        store_and_fwd_flag,
        ratecodeid,
        passenger_count,
        trip_distance,
        fare_amount,
        total_amount,
        payment_type,
        trip_type,
        improvement_surcharge,
        pulocationid,
        dolocationid

    from source
)

select * from renamed